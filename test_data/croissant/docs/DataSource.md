---
term: http://mlcommons.org/croissant/DataSource
---

`DataSource` is the class describing the data that can be extracted from files to populate a `RecordSet`. This class should be used when the data coming from the source needs to be transformed or formatted to be included in the ML dataset; otherwise a simple `Reference` can be used instead to point to the source.

`DataSource` is a subclass of [schema.org/Intangible](https://schema.org/Intangible).

## Properties

| Property | Expected Type | Cardinality | Description |
|----------|---------------|-------------|-------------|
| fileObject | Reference | ONE | The name of the referenced `FileObject` source of the data |
| fileSet | Reference | ONE | The name of the referenced `FileSet` source of the data |
| recordSet | Reference | ONE | The name of the referenced `RecordSet` source |
| extract | Extract | ONE | The extraction method from the provided source |
| transform | Transform | MANY | A transformation to apply on source data on top of the extracted method as specified through `extract`, e.g., a regular expression or JSON query |
| format | Format | ONE | A format to parse the values of the data from text, e.g., a date format or number format |

## Usage

`DataSource` is used within `Field` definitions to specify where the data for the field comes from and how it should be processed. The source can be a `FileObject`, `FileSet`, or another `RecordSet`, and the data can be extracted and transformed using the `extract`, `transform`, and `format` properties.

## Example

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

This example extracts filenames from a set of image files and applies a regular expression transformation to extract just the base filename without the path and extension.