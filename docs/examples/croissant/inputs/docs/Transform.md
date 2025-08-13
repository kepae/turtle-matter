---
term: http://mlcommons.org/croissant/Transform
---

Croissant supports a few simple transformations that can be applied on the source data. Transformations are used to modify extracted data before it's included in the final dataset.

## Supported Transformations

- **delimiter**: Split a string into an array using the supplied character
- **regex**: A regular expression to parse the data  
- **jsonQuery**: A JSON query to evaluate on the (JSON) data source

## Examples

### Regular Expression Transformation
```json
{
  "fileSet": {
    "@id": "files"
  },
  "extract": {
    "fileProperty": "filename"
  },
  "transform": {
    "regex": "^(train|val|test)2014/.*\\.jpg$"
  }
}
```

This example extracts filenames and applies a regex to parse training/validation/test split information.

### Filename Parsing
```json
{
  "source": {
    "fileSet": { "@id": "image-files" },
    "extract": {
      "fileProperty": "filename"
    },
    "transform": {
      "regex": "([^\\/]*)\\.jpg"
    }
  }
}
```

This extracts the base filename (without path and extension) from image files.

### Delimiter Transformation
```json
{
  "transform": {
    "delimiter": ","
  }
}
```

This would split a comma-separated string into an array of values.

### JSON Query Transformation
```json
{
  "transform": {
    "jsonQuery": "$.metadata.authors[*].name"
  }
}
```

This would extract all author names from a JSON structure using a JSON query.

## Usage

Transformations are typically used within `DataSource` definitions, applied after data extraction but before final formatting. They provide a way to clean, parse, or restructure data to make it suitable for machine learning workflows without requiring external preprocessing steps.