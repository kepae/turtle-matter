---
term: http://mlcommons.org/croissant/Extract
---

Sometimes, not all the data from the source is needed, but only a subset. The `Extract` class can be used to specify how to do that, depending on the type of the data.

## Extraction Methods

| Source type | Property | Expected property value | Result |
|-------------|----------|------------------------|--------|
| FileObject or FileSet | fileProperty | One of: `fullpath`, `filename`, `content`, `lines`, `lineNumbers` | The corresponding property for the FileObject |
| CSV (FileObject) | column | A column name | Values in the specified column |
| JSON | jsonPath | A [JSONPath](https://goessner.net/articles/JsonPath/) expression | The value(s) obtained by evaluating the JSON path expression |

## FileProperty Values

- **`fullpath`**: The full path to the file within the Croissant extraction or download folders. Example: `data/train/metadata.csv`
- **`filename`**: The name of the file. In `data/train/metadata.csv`, the file name is `metadata.csv`
- **`content`**: The byte content of the file
- **`lines`**: The byte content of each line in the file
- **`lineNumbers`**: The number of each line in the file (starting from 0)

## Examples

### Extracting File Content
```json
{
  "extract": {
    "fileProperty": "content"
  }
}
```

### Extracting CSV Column
```json
{
  "extract": {
    "column": "userId"
  }
}
```

### Extracting with JSONPath
```json
{
  "extract": {
    "jsonPath": "$.metadata.title"
  }
}
```

### Extracting Filename
```json
{
  "extract": {
    "fileProperty": "filename"
  }
}
```

This class is typically used within a `DataSource` to specify exactly what part of the source data should be extracted for a particular field.