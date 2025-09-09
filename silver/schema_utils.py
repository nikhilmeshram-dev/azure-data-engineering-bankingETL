

from pyspark.sql.types import StructType

def validate_schema(incoming_df, expected_schema: StructType, dataset_name: str):
    incoming_fields = {f.name: f.dataType for f in incoming_df.schema.fields}
    expected_fields = {f.name: f.dataType for f in expected_schema.fields}
    
    missing_cols = [col for col in expected_fields if col not in incoming_fields]
    extra_cols = [col for col in incoming_fields if col not in expected_fields]
    type_mismatches = [
        (col, str(expected_fields[col]), str(incoming_fields[col]))
        for col in expected_fields
        if col in incoming_fields and incoming_fields[col] != expected_fields[col]
    ]
    
    if missing_cols or extra_cols or type_mismatches:
        msg = f"❌ Schema validation failed for {dataset_name}\n"
        if missing_cols:
            msg += f"   - Missing columns: {missing_cols}\n"
        if extra_cols:
            msg += f"   - Extra columns: {extra_cols}\n"
        if type_mismatches:
            msg += f"   - Datatype mismatches: {type_mismatches}\n"
        raise Exception(msg)
    else:
        print(f"✅ {dataset_name} schema validated successfully")
