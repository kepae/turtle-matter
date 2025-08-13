---
term: http://mlcommons.org/croissant/Format
---

A format string used to parse the values coming from a `DataSource`. For example, a date may be represented as the string "2022/11/10", and interpreted into the correct date via the format "yyyy/MM/dd". Formats correspond to a target data type.

## Supported Format Types

| Data types | Format | Example |
|------------|--------|---------|
| [sc:Date](http://schema.org/Date)<br>[sc:DateTime](http://schema.org/DateTime) | [CLDR Date/Time Patterns](https://cldr.unicode.org/translation/date-time/date-time-patterns) | MM/dd/yyyy |
| [sc:Number](http://schema.org/Number)<br>[sc:Float](http://schema.org/Float)<br>[sc:Integer](http://schema.org/Integer) | [CLDR Number and Currency patterns](https://cldr.unicode.org/translation/number-currency-formats/number-and-currency-patterns) | 0.##E0 (scientific notation with max 2 decimals) |
| cr:BoundingBox | [Keras bounding box format](https://keras.io/api/keras_cv/bounding_box/formats/) | CENTER_XYWH |

**Note**: This list is not exhaustive, and not all Croissant implementations will support all formats.

## Examples

### Date Format Parsing
```json
{
  "source": {
    "fileObject": { "@id": "metadata" },
    "extract": { "column": "datetaken" },
    "format": "%Y-%m-%d %H:%M:%S.%f"
  }
}
```

### Bounding Box Format
```json
{
  "@type": "cr:Field",
  "@id": "images/annotations/bbox",
  "description": "The bounding box around annotated object[s].",
  "dataType": "cr:BoundingBox",
  "source": {
    "fileSet": { "@id": "instancesperson_keypoints_annotations" },
    "extract": { "column": "bbox" },
    "format": "CENTER_XYWH"
  }
}
```

## Usage

Format specifications are typically used within `DataSource` definitions to ensure that string representations of structured data (like dates, numbers, or coordinates) are correctly parsed into their intended data types. This is particularly important for ML datasets where precise data interpretation is crucial for model training and evaluation.