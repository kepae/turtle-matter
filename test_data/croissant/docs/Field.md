---
term: http://mlcommons.org/croissant/Field
---

A `Field` is part of a `RecordSet`. It may represent a column of a table, or a nested data structure or even a nested `RecordSet` in the case of hierarchical data.

`Field` is a subclass of [schema.org/Intangible](https://schema.org/Intangible).

## Properties

| Property | Expected Type | Cardinality | Description |
|----------|---------------|-------------|-------------|
| source | DataSource<br>[URL](http://schema.org/URL) | ONE | The data source of the field. This will generally reference a `FileObject` or `FileSet`'s contents |
| dataType | DataType | MANY | The data type of the field, identified by the URI of the corresponding class |
| repeated | [Boolean](http://schema.org/Boolean) | ONE | If true, then the Field is a list of values of type dataType |
| equivalentProperty | [URL](http://schema.org/URL) | MANY | A property that is equivalent to this Field |
| references | Reference | MANY | Another `Field` of another `RecordSet` that this field references (foreign key equivalent) |
| subField | Field | MANY | Another `Field` that is nested inside this one |
| parentField | Reference | MANY | A special case of `SubField` that should be hidden because it references a `Field` that already appears in the `RecordSet` |

## Key Features

- Each field has a `name` (unique identifier within the `RecordSet`)
- Supports foreign key relationships through the `references` property
- Supports hierarchical nesting with `subField` and `parentField`
- Can specify multiple data types for semantic enrichment

## Examples

### Simple Field
```json
{
  "@type": "cr:Field",
  "@id": "ratings/user_id",
  "dataType": "sc:Integer",
  "source": {
    "fileObject": { "@id": "ratings-table" },
    "extract": {
      "column": "userId"
    }
  }
}
```

### Field with Reference (Foreign Key)
```json
{
  "@type": "cr:Field",
  "@id": "ratings/movie_id",
  "dataType": "sc:Integer",
  "source": {
    "fileObject": { "@id": "ratings-table" },
    "extract": {
      "column": "movieId"
    }
  },
  "references": {
    "@id": "movies/movie_id"
  }
}
```

### Nested Field with SubFields
```json
{
  "@type": "cr:Field",
  "@id": "gps_coordinates",
  "description": "GPS coordinates where the image was taken.",
  "dataType": "sc:GeoCoordinates",
  "subField": [
    {
      "@type": "cr:Field",
      "@id": "gps_coordinates/latitude",
      "dataType": "sc:Float",
      "source": {
        "fileObject": { "@id": "metadata" },
        "extract": { "column": "latitude" }
      }
    },
    {
      "@type": "cr:Field",
      "@id": "gps_coordinates/longitude",
      "dataType": "sc:Float",
      "source": {
        "fileObject": { "@id": "metadata" },
        "extract": { "column": "longitude" }
      }
    }
  ]
}
```

This example shows how fields can be hierarchically structured to represent complex data types like geographical coordinates.