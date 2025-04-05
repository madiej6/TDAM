import argparse
from classify import classify_structures
from validate import validate_mappings
from utils.duckdb import initialize

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--id',
                        dest='id',
                        type=str,
                        required=True,
                        help='Unique identifier for the current project/tornado. All outputs will be named using this ID.')

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--classify-structures',
                       dest='structures_path',
                       type=str,
                       help='Path to the structures dataset to classify.')
    
    group.add_argument('--validate-mappings', 
                       dest='validate',
                       help='Run the validator on your structure mappings.',
                       action='store_true')
    
    parser.add_argument('--type-col',
                        dest='type_col',
                        type=str,
                        help='Name of the column that contains building types (required with --classify-buildings).')

    parser.add_argument('--rebuild-tables', 
                       dest='rebuild',
                       help='Rebuild helper tables. Run if you made changes to the damage tables.',
                       action='store_true')
    
    args = parser.parse_args()

    tdam_id = args.id
    validate = args.validate
    structures_path = args.structures_path
    type_col = args.type_col
    rebuild = args.rebuild

    if rebuild:
        initialize(rebuild)

    if structures_path and not type_col:
        parser.error("--type-col is required when using --classify-structures.")


    if structures_path:
        classify_structures(structures_path, type_col, tdam_id)

    if validate:
        validate_mappings(tdam_id)
