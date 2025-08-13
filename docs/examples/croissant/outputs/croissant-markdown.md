---
title: Croissant
namespace: http://mlcommons.org/croissant/
generator: turtle-matter v0.1.0
jsonld_context: |
  {
    "@context": {
      "@vocab": "http://mlcommons.org/croissant/",
      "schema": "https://schema.org/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "ContentExtractionEnumeration": {
        "@id": "http://mlcommons.org/croissant/ContentExtractionEnumeration",
        "@type": "@id"
      },
      "DataSource": {
        "@id": "http://mlcommons.org/croissant/DataSource",
        "@type": "@id"
      },
      "DataType": {
        "@id": "http://mlcommons.org/croissant/DataType",
        "@type": "@id"
      },
      "Extract": {
        "@id": "http://mlcommons.org/croissant/Extract",
        "@type": "@id"
      },
      "Field": {
        "@id": "http://mlcommons.org/croissant/Field",
        "@type": "@id"
      },
      "FileObject": {
        "@id": "http://mlcommons.org/croissant/FileObject",
        "@type": "@id"
      },
      "FilePropertyEnumeration": {
        "@id": "http://mlcommons.org/croissant/FilePropertyEnumeration",
        "@type": "@id"
      },
      "FileSet": {
        "@id": "http://mlcommons.org/croissant/FileSet",
        "@type": "@id"
      },
      "Format": {
        "@id": "http://mlcommons.org/croissant/Format",
        "@type": "@id"
      },
      "RecordSet": {
        "@id": "http://mlcommons.org/croissant/RecordSet",
        "@type": "@id"
      },
      "Transform": {
        "@id": "http://mlcommons.org/croissant/Transform",
        "@type": "@id"
      },
      "citeAs": {
        "@id": "http://mlcommons.org/croissant/citeAs"
      },
      "column": {
        "@id": "http://mlcommons.org/croissant/column"
      },
      "containedIn": {
        "@id": "http://mlcommons.org/croissant/containedIn"
      },
      "content": {
        "@id": "http://mlcommons.org/croissant/content"
      },
      "data": {
        "@id": "http://mlcommons.org/croissant/data"
      },
      "dataType": {
        "@id": "http://mlcommons.org/croissant/dataType"
      },
      "delimiter": {
        "@id": "http://mlcommons.org/croissant/delimiter"
      },
      "equivalentProperty": {
        "@id": "http://mlcommons.org/croissant/equivalentProperty"
      },
      "examples": {
        "@id": "http://mlcommons.org/croissant/examples"
      },
      "excludes": {
        "@id": "http://mlcommons.org/croissant/excludes"
      },
      "extract": {
        "@id": "http://mlcommons.org/croissant/extract"
      },
      "field": {
        "@id": "http://mlcommons.org/croissant/field"
      },
      "fileObject": {
        "@id": "http://mlcommons.org/croissant/fileObject"
      },
      "fileProperty": {
        "@id": "http://mlcommons.org/croissant/fileProperty"
      },
      "fileSet": {
        "@id": "http://mlcommons.org/croissant/fileSet"
      },
      "format": {
        "@id": "http://mlcommons.org/croissant/format"
      },
      "includes": {
        "@id": "http://mlcommons.org/croissant/includes"
      },
      "isLiveDataset": {
        "@id": "http://mlcommons.org/croissant/isLiveDataset"
      },
      "jsonPath": {
        "@id": "http://mlcommons.org/croissant/jsonPath"
      },
      "jsonQuery": {
        "@id": "http://mlcommons.org/croissant/jsonQuery"
      },
      "key": {
        "@id": "http://mlcommons.org/croissant/key"
      },
      "parentField": {
        "@id": "http://mlcommons.org/croissant/parentField"
      },
      "recordSet": {
        "@id": "http://mlcommons.org/croissant/recordSet"
      },
      "references": {
        "@id": "http://mlcommons.org/croissant/references"
      },
      "regex": {
        "@id": "http://mlcommons.org/croissant/regex"
      },
      "repeated": {
        "@id": "http://mlcommons.org/croissant/repeated"
      },
      "source": {
        "@id": "http://mlcommons.org/croissant/source"
      },
      "subField": {
        "@id": "http://mlcommons.org/croissant/subField"
      },
      "transform": {
        "@id": "http://mlcommons.org/croissant/transform"
      }
    }
  }
---

# Croissant

**Namespace:** http://mlcommons.org/croissant/

## Classes (11)

### ContexExtractionEnumeration

**URI:** `http://mlcommons.org/croissant/ContentExtractionEnumeration`

**Description:** Specifies which content to extract from a file. One of "all", "lines", or "lineNumbers".

**Subclass of:**
- [https://schema.org/Enumeration](https://schema.org/Enumeration)

---

### DataSource

**URI:** `http://mlcommons.org/croissant/DataSource`

**Description:** A source of data, optionally transformed before being used.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [extract](#extract) (→ Extract)
- [fileObject](#fileObject) (→ FileObject)
- [fileSet](#fileSet) (→ FileSet)
- [format](#format) (→ Format)
- [recordSet](#recordSet) (→ RecordSet)
- [transform](#transform) (→ Transform)

**Documentation:**

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

---

### DataType

**URI:** `http://mlcommons.org/croissant/DataType`

**Description:** The data type of values expected for a Field in a RecordSet. This class is inspired by the Datatype class in CSVW. In addition to simple atomic types, types can be semantic types, such as schema.org classes, as well types defined in other vocabularies.

**Subclass of:**
- [https://schema.org/URL](https://schema.org/URL)

**Documentation:**

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

---

### Extract

**URI:** `http://mlcommons.org/croissant/Extract`

**Description:** Specifies how to extract data from a DataSource. The extraction mechanism depends on the type of content, e.g., a column name for tabular data, or a jsonPath for JSON data.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [column](#column) (→ Text)
- [content](#content) (→ ContentExtractionEnumeration)
- [fileProperty](#fileProperty) (→ FilePropertyEnumeration)
- [jsonPath](#jsonPath) (→ Text)

**Documentation:**

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

---

### Field

**URI:** `http://mlcommons.org/croissant/Field`

**Description:** A component of the structure of a RecordSet, such as a column of a table.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [dataType](#dataType) (→ DataType)
- [equivalentProperty](#equivalentProperty) (→ URL)
- [parentField](#parentField) (→ Field)
- [references](#references) (→ Field)
- [repeated](#repeated) (→ Boolean)
- [source](#source) (→ DataSource, FileObject, FileSet, RecordSet)
- [subField](#subField) (→ Field)

**Documentation:**

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

---

### FileObject

**URI:** `http://mlcommons.org/croissant/FileObject`

**Description:** An individual file that is part of a dataset.

**Subclass of:**
- [https://schema.org/CreativeWork](https://schema.org/CreativeWork)

**Properties:**
- [containedIn](#containedIn) (→ FileObject, FileSet)

**Documentation:**

`FileObject` is the Croissant class used to represent individual files that are part of a dataset.

`FileObject` is a general purpose class that inherits from [Schema.org](http://Schema.org) `CreativeWork`, and can be used to represent instances of more specific types of content like `DigitalDocument` and `MediaObject`.

Most of the important properties needed to describe a `FileObject` are defined in the classes it inherits from:

<table>
  <thead>
    <th>Property</th>
    <th>ExpectedType</th>
    <th>Cardinality</th>
    <th>Description</th>
  </thead>
  <tr>
    <td><a href="https://schema.org/name">sc:name</a></td>
    <td><a href="http://schema.org/Text">Text</a></td>
    <td>ONE</td>
    <td>The name of the file. As much as possible, the name should reflect the name of the file as downloaded, including the file extension. e.g. "images.zip".</td>
  </tr>
  <tr>
    <td><a href="https://schema.org/contentUrl">sc:contentUrl</a></td>
    <td><a href="http://schema.org/URL">URL</a></td>
    <td>ONE</td>
    <td>Actual bytes of the media object, for example the image file or video file.</td>
  </tr>
  <tr>
    <td><a href="https://schema.org/contentSize">sc:contentSize</a></td>
    <td><a href="http://schema.org/Text">Text</a></td>
    <td>ONE</td>
    <td>File size in (mega/kilo/…)bytes. Defaults to bytes if a unit is not specified.</td>
  </tr>
  <tr>
    <td><a href="https://schema.org/encodingFormat">sc:encodingFormat</a></td>
    <td><a href="http://schema.org/Text">Text</a></td>
    <td>ONE</td>
    <td>The format of the file, given as a mime type.</td>
  </tr>
  <tr>
    <td><a href="https://schema.org/sameAs">sc:sameAs</a></td>
    <td><a href="http://schema.org/URL">URL</a></td>
    <td>MANY</td>
    <td>URL (or local name) of a FileObject with the same content, but in a different format.</td>
  </tr>
  <tr>
    <td><a href="https://schema.org/sha256">sc:sha256</a></td>
    <td><a href="http://schema.org/Text">Text</a></td>
    <td>ONE</td>
    <td>Checksum for the file contents.</td>
  </tr>
</table>

In addition, `FileObject` defines the following property:

<table>
  <thead>
    <th>Property</th>
    <th>ExpectedType</th>
    <th>Cardinality</th>
    <th>Description</th>
  </thead>
  <tr>
    <td>containedIn</td>
    <td><a href="http://schema.org/Text">Text</a></td>
    <td>MANY</td>
    <td>Another <code>FileObject</code> or <code>FileSet</code> that this one is contained in, e.g., in the case of a file extracted from an archive. When this property is present, the <code>contentUrl</code> is evaluated as a relative path within the container object.</td>
  </tr>
</table>

Let's look at a few examples of `FileObject` definitions.

First, a single CSV file:

```json
{
  "@type": "cr:FileObject",
  "@id": "pass_metadata.csv",
  "contentUrl": "https://zenodo.org/record/6615455/files/pass_metadata.csv",
  "encodingFormat": "text/csv",
  "sha256": "0b033707ea49365a5ffdd14615825511"
}
```

Next: An archive and some files extracted from it (represented via the `containedIn` property):

```json
{
  "@type": "cr:FileObject",
  "@id": "ml-25m.zip",
  "contentUrl": "https://files.grouplens.org/datasets/movielens/ml-25m.zip",
  "encodingFormat": "application/zip",
  "sha256": "6b51fb2759a8657d3bfcbfc42b592ada"
},
{
  "@type": "cr:FileObject",
  "@id": "ratings-table",
  "contentUrl": "ratings.csv",
  "containedIn": { "@id": "ml-25m.zip" },
  "encodingFormat": "text/csv"
},
{
  "@type": "cr:FileObject",
  "@id": "movies-table",
  "contentUrl": "movies.csv",
  "containedIn": { "@id": "ml-25m.zip" },
  "encodingFormat": "text/csv"
}
```

---

### FilePropertyEnumeration

**URI:** `http://mlcommons.org/croissant/FilePropertyEnumeration`

**Description:** Specifies a property of a FileObject. One of "fullPath" or "fileName".

**Subclass of:**
- [https://schema.org/Enumeration](https://schema.org/Enumeration)

---

### FileSet

**URI:** `http://mlcommons.org/croissant/FileSet`

**Description:** A set of homogeneous files extracted from a container, optionally filtered by inclusion and/or exclusion filters.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [containedIn](#containedIn) (→ FileObject, FileSet)
- [excludes](#excludes) (→ Text)
- [includes](#includes) (→ Text)

**Documentation:**

In many datasets, data comes in the form of collections of homogeneous files, such as images, videos or text files, where each file needs to be treated as an individual item, e.g., as a training example. `FileSet` is a class that describes such collections of files.

A `FileSet` is a set of files located in a container, which can be an archive `FileObject` or a "manifest" file. A FileSet may also specify inclusion / exclusion filters using file patterns.

`FileSet` extends [schema.org/Intangible](https://schema.org/Intangible).

## Properties

| Property | Expected Type | Cardinality | Description |
|----------|---------------|-------------|-------------|
| containedIn | Reference | MANY | The source of data for the `FileSet`, e.g., an archive. If multiple values are provided, then the union of their contents is taken |
| includes | [Text](http://schema.org/Text) | MANY | A glob pattern that specifies the files to include |
| excludes | [Text](http://schema.org/Text) | MANY | A glob pattern that specifies the files to exclude |

## Pattern Processing

The `includes` and `excludes` properties use [glob patterns](https://en.wikipedia.org/wiki/Glob_(programming)), a common mechanism to specify a set of files along a path, like "*.jpg" for all jpg images, or "/foo/pic*.jpg" for all jpg images under the "foo" directory whose filename starts with "pic".

To get the set of FileObjects included in the FileSet:
1. The `includes` pattern(s) are evaluated first
2. If multiple `includes` are specified, the union of their results is taken
3. Then all the files corresponding to the `excludes` patterns are removed from that set
4. Patterns are evaluated from the root of the `containedIn` contents (e.g., the top level directory extracted from an archive)

## Examples

### Simple Image Archive
```json
{
  "@type": "cr:FileObject",
  "@id": "train2014.zip",
  "contentSize": "13510573713 B",
  "contentUrl": "http://images.cocodataset.org/zips/train2014.zip",
  "encodingFormat": "application/zip",
  "sha256": "sha256"
},
{
  "@type": "cr:FileSet",
  "@id": "image-files",
  "containedIn": { "@id": "train2014.zip" },
  "encodingFormat": "image/jpeg",
  "includes": "*.jpg"
}
```

### Complex Archive with Multiple FileSets
```json
{
  "@type": "cr:FileObject",
  "@id": "flores200_dataset.tar.gz",
  "description": "Flores 200 is hosted on a webserver.",
  "contentSize": "25585843 B",
  "contentUrl": "https://tinyurl.com/flores200dataset",
  "encodingFormat": "application/x-gzip",
  "sha256": "c764ffdeee4894b3002337c5b1e70ecf6f514c00"
},
{
  "@type": "cr:FileSet",
  "@id": "files-dev",
  "description": "dev files are inside the tar.",
  "containedIn": { "@id": "flores200_dataset.tar.gz" },
  "encodingFormat": "application/json",
  "includes": "flores200_dataset/dev/*.dev"
},
{
  "@type": "cr:FileSet",
  "@id": "files-devtest",
  "description": "devtest files are inside the tar.",
  "containedIn": { "@id": "flores200_dataset.tar.gz" },
  "encodingFormat": "application/json",
  "includes": "flores200_dataset/devtest/*.devtest"
}
```

This example shows how multiple FileSets can be extracted from a single archive, each with different inclusion patterns to select different subsets of files.

---

### Format

**URI:** `http://mlcommons.org/croissant/Format`

**Description:** Specifies how to parse the format of the data from a string representation. For example, format may hold a date format string, a number format, or a bounding box format.

**Subclass of:**
- [https://schema.org/Text](https://schema.org/Text)

**Documentation:**

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

---

### RecordSet

**URI:** `http://mlcommons.org/croissant/RecordSet`

**Description:** A description of a set of structured records from one or more data sources and their structure, expressed as a set of fields.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [data](#data) (→ 22-rdf-syntax-ns#JSON)
- [dataType](#dataType) (→ DataType)
- [examples](#examples) (→ 22-rdf-syntax-ns#JSON)
- [field](#field) (→ Field)
- [key](#key) (→ Field)
- [source](#source) (→ DataSource, FileObject, FileSet, RecordSet)

**Documentation:**

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

---

### Transform

**URI:** `http://mlcommons.org/croissant/Transform`

**Description:** Specifies how to transform data extracted from a DataSource. The type of transformation depends on the type of content, e.g., a regular expression to appy on text, or a jsonQuery to transform JSON content.

**Subclass of:**
- [https://schema.org/Intangible](https://schema.org/Intangible)

**Properties:**
- [delimiter](#delimiter) (→ Text)
- [jsonQuery](#jsonQuery) (→ Text)
- [regex](#regex) (→ Text)

**Documentation:**

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

---

## Properties (29)

### citeAs

**URI:** `http://mlcommons.org/croissant/citeAs`

**Description:** How to cite this dataset. Ideally, citations should be expressed using the bibtex format. Note that this is different from schema.org/citation, which is used to make a citation to another publication from this dataset.

**Domain:**
- [https://schema.org/Dataset](https://schema.org/Dataset)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### column

**URI:** `http://mlcommons.org/croissant/column`

**Description:** In case the data source is tabular, the id of a column to extract.

**Domain:**
- [http://mlcommons.org/croissant/Extract](http://mlcommons.org/croissant/Extract)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### containedIn

**URI:** `http://mlcommons.org/croissant/containedIn`

**Description:** Another FileObject or FileSet that this one is contained in, e.g., in the case of a file extracted from an archive. When this property is present, the contentUrl is evaluated as a relative path within the container object.

**Domain:**
- [http://mlcommons.org/croissant/FileObject](http://mlcommons.org/croissant/FileObject)
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

**Range:**
- [http://mlcommons.org/croissant/FileObject](http://mlcommons.org/croissant/FileObject)
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

---

### content

**URI:** `http://mlcommons.org/croissant/content`

**Description:** What to extract from the data source content, e.g., lines.

**Domain:**
- [http://mlcommons.org/croissant/Extract](http://mlcommons.org/croissant/Extract)

**Range:**
- [http://mlcommons.org/croissant/ContentExtractionEnumeration](http://mlcommons.org/croissant/ContentExtractionEnumeration)

---

### data

**URI:** `http://mlcommons.org/croissant/data`

**Description:** One or more inlined records that constitute the data of the RecordSet, typically used for small enumeration values.

**Domain:**
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON](http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON)

---

### dataType

**URI:** `http://mlcommons.org/croissant/dataType`

**Description:** The data type of the field, identified by the URI of the corresponding class. It could be either an atomic type (e.g, sc:Integer) or a semantic type (e.g., sc:GeoLocation).

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://mlcommons.org/croissant/DataType](http://mlcommons.org/croissant/DataType)

---

### delimiter

**URI:** `http://mlcommons.org/croissant/delimiter`

**Description:** A delimiter to use parse the data into an array.

**Domain:**
- [http://mlcommons.org/croissant/Transform](http://mlcommons.org/croissant/Transform)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### equivalentProperty

**URI:** `http://mlcommons.org/croissant/equivalentProperty`

**Description:** A property that is equivalent to this Field. Used in the case a dataType is specified on the RecordSet to map specific fields to specific properties associated with that dataType.

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

**Range:**
- [https://schema.org/URL](https://schema.org/URL)

---

### examples

**URI:** `http://mlcommons.org/croissant/examples`

**Description:** One more inlined records provided as example content of the RecordSet.

**Domain:**
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON](http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON)

---

### excludes

**URI:** `http://mlcommons.org/croissant/excludes`

**Description:** A glob pattern that specifies the files to exclude. The pattern is evaluated from the root of the containedIn contents, after the includes patterns have been evaluated.

**Domain:**
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### extract

**URI:** `http://mlcommons.org/croissant/extract`

**Description:** The extraction method from the provided source.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/Extract](http://mlcommons.org/croissant/Extract)

---

### field

**URI:** `http://mlcommons.org/croissant/field`

**Description:** A data element that appears in the records of the RecordSet (e.g., one column of a table).

**Domain:**
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

---

### fileObject

**URI:** `http://mlcommons.org/croissant/fileObject`

**Description:** The id of a FileObject that is the source of the data.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/FileObject](http://mlcommons.org/croissant/FileObject)

---

### fileProperty

**URI:** `http://mlcommons.org/croissant/fileProperty`

**Description:** The file property to extract from the data source metadata, e.g., the filename.

**Domain:**
- [http://mlcommons.org/croissant/Extract](http://mlcommons.org/croissant/Extract)

**Range:**
- [http://mlcommons.org/croissant/FilePropertyEnumeration](http://mlcommons.org/croissant/FilePropertyEnumeration)

---

### fileSet

**URI:** `http://mlcommons.org/croissant/fileSet`

**Description:** The id of a FileSet that is the source of the data.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

---

### format

**URI:** `http://mlcommons.org/croissant/format`

**Description:** A format to parse the values of the data from text, e.g., a date format or number format.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/Format](http://mlcommons.org/croissant/Format)

---

### includes

**URI:** `http://mlcommons.org/croissant/includes`

**Description:** A glob pattern that specifies the files to include, e.g., ".jpg", "/foo/pic*.jpg". The pattern is evaluated from the root of the containedIn contents.

**Domain:**
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### isLiveDataset

**URI:** `http://mlcommons.org/croissant/isLiveDataset`

**Description:** Indicates that the dataset is continuously updated instead of being versioned.

**Domain:**
- [https://schema.org/Dataset](https://schema.org/Dataset)

**Range:**
- [https://schema.org/Boolean](https://schema.org/Boolean)

---

### jsonPath

**URI:** `http://mlcommons.org/croissant/jsonPath`

**Description:** In case the data source is JSON data, a path expression to extract a subset of the data.

**Domain:**
- [http://mlcommons.org/croissant/Extract](http://mlcommons.org/croissant/Extract)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### jsonQuery

**URI:** `http://mlcommons.org/croissant/jsonQuery`

**Description:** For JSON content, a query to evaluate on the data.

**Domain:**
- [http://mlcommons.org/croissant/Transform](http://mlcommons.org/croissant/Transform)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### key

**URI:** `http://mlcommons.org/croissant/key`

**Description:** One or more fields whose values uniquely identify each record in the RecordSet. (See example below.)

**Domain:**
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

---

### parentField

**URI:** `http://mlcommons.org/croissant/parentField`

**Description:** A special case of SubField that should be hidden because it references a Field that already appears in the RecordSet.

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

**Range:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

---

### recordSet

**URI:** `http://mlcommons.org/croissant/recordSet`

**Description:** The id of a RecordSet that is the source of the data.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

---

### references

**URI:** `http://mlcommons.org/croissant/references`

**Description:** Another Field of another RecordSet that this field references. This is the equivalent of a foreign key reference in a relational database.

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

**Range:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

---

### regex

**URI:** `http://mlcommons.org/croissant/regex`

**Description:** A regular expression to apply to the data.

**Domain:**
- [http://mlcommons.org/croissant/Transform](http://mlcommons.org/croissant/Transform)

**Range:**
- [https://schema.org/Text](https://schema.org/Text)

---

### repeated

**URI:** `http://mlcommons.org/croissant/repeated`

**Description:** If true, then the Field is a list of values of type dataType.

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

**Range:**
- [https://schema.org/Boolean](https://schema.org/Boolean)

---

### source

**URI:** `http://mlcommons.org/croissant/source`

**Description:** The data source of the field. This will generally reference a FileObject or FileSet's contents (e.g., a specific column of a table).

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

**Range:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)
- [http://mlcommons.org/croissant/FileObject](http://mlcommons.org/croissant/FileObject)
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)

---

### subField

**URI:** `http://mlcommons.org/croissant/subField`

**Description:** Another Field that is nested inside this one.

**Domain:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

**Range:**
- [http://mlcommons.org/croissant/Field](http://mlcommons.org/croissant/Field)

---

### transform

**URI:** `http://mlcommons.org/croissant/transform`

**Description:** A transformation to apply on source data on top of the extracted method as specified through extract, e.g., a regular expression or JSON query.

**Domain:**
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)

**Range:**
- [http://mlcommons.org/croissant/Transform](http://mlcommons.org/croissant/Transform)

---

---

🐢 *Generated with [turtle-matter](https://github.com/kepae/turtle-matter) v0.1.0*

