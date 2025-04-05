import os
from utils.duckdb import initialize
from utils.logging import get_logger


def validate_mappings(tdam_id: str):

    logger = get_logger(__name__)
    logger.info("Validating structure mappings.")

    csv_to_validate = os.path.join(os.getcwd(), 'tables', f'structural_mappings_{tdam_id}.csv')

    conn = initialize()
    conn.execute(f"CREATE OR REPLACE TABLE structure_mappings_{tdam_id} AS SELECT * FROM read_csv('{csv_to_validate}')")

    sql = f"""
    SELECT DISTINCT sm.DamageIndicator
    FROM structure_mappings_{tdam_id} sm
    LEFT JOIN damage_indicators di
    ON sm.DamageIndicator = di.ABBREVIATION
    WHERE di.ABBREVIATION IS NULL;
    """

    result = conn.query(sql).fetchall()
    assert len(result) == 0, f"Structure mappings csv ({os.path.basename(csv_to_validate)}) contains invalid DamageIndicators: {result}"

    logger.info("Validator passed.")