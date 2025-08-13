---
term: http://mlcommons.org/croissant/DataType
---

The data type of values expected for a `Field` in a `RecordSet`. This class is inspired by the Datatype class in [CSVW](https://csvw.org/). In addition to simple atomic types, types can be semantic types, such as schema.org classes, as well types defined in other vocabularies.

## Key Features

- A field may have more than a single assigned `dataType`, in which case at least one must be an atomic data type (e.g.: `sc:Text`), while other types can provide more semantic information, possibly in the context of ML.
- Can be specified at two levels: on individual `Field`s and on entire `RecordSet`s.

## Atomic Data Types

| dataType | Usage |
|----------|-------|
| [sc:Boolean](https://schema.org/Boolean) | Describes a boolean |
| [sc:Date](https://schema.org/Date) | Describes a date |
| [sc:Float](https://schema.org/Float) | Describes a float |
| [sc:Integer](https://schema.org/Integer) | Describes an integer |
| [sc:Text](https://schema.org/Text) | Describes a string |

## ML-Specific Data Types

| dataType | Usage |
|----------|-------|
| [sc:ImageObject](https://schema.org/ImageObject) | Describes a field containing the content of an image (pixels) |
| [cr:BoundingBox](http://mlcommons.org/schema/BoundingBox) | Describes the coordinates of a bounding box (4-number array) |
| [cr:Split](http://mlcommons.org/schema/Split) | Describes a RecordSet used to divide data into multiple sets according to intended usage with regards to models |

## Using Data Types from Other Vocabularies

Croissant datasets can use data types from other vocabularies, such as Wikidata. These may be supported by the tools consuming the data, but don't need to. For example:

| dataType | Usage |
|----------|-------|
| [wd:Q48277](https://www.wikidata.org/wiki/Q48277) (gender) | Describes a Field or a RecordSet whose values are indicative of someone's gender |

## Examples

### Simple Field Type
```json
{
  "@id": "images/color_sample",
  "@type": "cr:Field",
  "dataType": "sc:ImageObject"
}
```

### Multiple Data Types
```json
{
  "@id": "cities/url",
  "@type": "cr:Field",
  "dataType": ["https://schema.org/URL", "https://www.wikidata.org/wiki/Q515"]
}
```

This example shows a field that is expected to be a URL, whose semantic type is City, so values will be URLs referring to cities.