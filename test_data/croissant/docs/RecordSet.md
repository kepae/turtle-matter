---
term: http://mlcommons.org/croissant/RecordSet
---

A `RecordSet` describes a set of structured records obtained from one or more data sources (typically a file or set of files) and the structure of these records, expressed as a set of fields (e.g., the columns of a table). A `RecordSet` can represent flat or nested data.

## Purpose

`RecordSet` provides a common structure description that can be used across different modalities, in terms of records that may contain multiple fields. It handles:

- **Unstructured content** (like text and images) as single-field records
- **Tabular data** as one record per row in the table, with fields for each column  
- **Tree-structured data** with nested and repeated fields

`RecordSet` is a subclass of [schema.org/Intangible](https://schema.org/Intangible).

## Properties

| Property | Expected Type | Cardinality | Description |
|----------|---------------|-------------|-------------|
| field | Field | MANY | A data element that appears in the records of the `RecordSet` (e.g., one column of a table) |
| key | [Text](http://schema.org/Text) | MANY | One or more fields whose values uniquely identify each record in the `RecordSet` |
| data | JSON | MANY | One or more records that constitute the data of the `RecordSet` |
| examples | JSON<br>[URL](http://schema.org/URL) | MANY | One or more records provided as example content of the `RecordSet`, or a reference to data source that contains examples |

## Additional Features

- **Embedding**: Supports embedding small enumerations directly via the `data` property
- **Typing**: Supports typing with `dataType` for entire RecordSets  
- **Joins**: Supports joins through field references (foreign keys)
- **Hierarchical**: Supports hierarchical structures with nested records

## Examples

### Simple Tabular RecordSet
```json
{
  "@type": "cr:RecordSet",
  "@id": "ratings",
  "key": [{ "@id": "ratings/user_id" }, { "@id": "ratings/movie_id" }],
  "field": [
    {
      "@type": "cr:Field",
      "@id": "ratings/user_id",
      "dataType": "sc:Integer",
      "source": {
        "fileObject": { "@id": "ratings-table" },
        "extract": { "column": "userId" }
      }
    },
    {
      "@type": "cr:Field",
      "@id": "ratings/rating",
      "description": "The score of the rating on a five-star scale.",
      "dataType": "sc:Float",
      "source": {
        "fileObject": { "@id": "ratings-table" },
        "extract": { "column": "rating" }
      }
    }
  ]
}
```

### Enumeration with Embedded Data
```json
{
  "@type": "cr:RecordSet",
  "@id": "gender_enum",
  "description": "Maps gender ids (0, 1) to labeled values.",
  "key": { "@id": "gender_enum/id" },
  "field": [
    { "@id": "gender_enum/id", "@type": "cr:Field", "dataType": "sc:Integer" },
    { "@id": "gender_enum/label", "@type": "cr:Field", "dataType": "sc:String" }
  ],
  "data": [
    { "gender_enum/id": 0, "gender_enum/label": "Male" },
    { "gender_enum/id": 1, "gender_enum/label": "Female" }
  ]
}
```

### Geographic Data with Type Mapping
```json
{
  "@id": "cities",
  "@type": "cr:RecordSet",
  "dataType": "sc:GeoCoordinates",
  "field": [
    {
      "@id": "cities/latitude",
      "@type": "cr:Field"
    },
    {
      "@id": "cities/longitude", 
      "@type": "cr:Field"
    }
  ]
}
```

This example shows how RecordSets can be typed with semantic types like `sc:GeoCoordinates`, and fields can be implicitly mapped to properties of that type (latitude and longitude).