---
title: Vocabulary
namespace: http://mlcommons.org/croissant/
jsonld_context: |
  {
    "@context": {
      "@vocab": "http://mlcommons.org/croissant/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "owl": "http://www.w3.org/2002/07/owl#",
      "schema": "https://schema.org/",
      "ContentExtractionEnumeration": {
        "@id": "http://mlcommons.org/croissant/ContentExtractionEnumeration",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Enumeration"
        }
      },
      "DataSource": {
        "@id": "http://mlcommons.org/croissant/DataSource",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "DataType": {
        "@id": "http://mlcommons.org/croissant/DataType",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/URL"
        }
      },
      "Extract": {
        "@id": "http://mlcommons.org/croissant/Extract",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "Field": {
        "@id": "http://mlcommons.org/croissant/Field",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "FileObject": {
        "@id": "http://mlcommons.org/croissant/FileObject",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/CreativeWork"
        }
      },
      "FilePropertyEnumeration": {
        "@id": "http://mlcommons.org/croissant/FilePropertyEnumeration",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Enumeration"
        }
      },
      "FileSet": {
        "@id": "http://mlcommons.org/croissant/FileSet",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "Format": {
        "@id": "http://mlcommons.org/croissant/Format",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Text"
        }
      },
      "RecordSet": {
        "@id": "http://mlcommons.org/croissant/RecordSet",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "Transform": {
        "@id": "http://mlcommons.org/croissant/Transform",
        "@type": "@id",
        "rdfs:subClassOf": {
          "@id": "https://schema.org/Intangible"
        }
      },
      "citeAs": {
        "@id": "http://mlcommons.org/croissant/citeAs",
        "rdfs:domain": {
          "@id": "https://schema.org/Dataset"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "column": {
        "@id": "http://mlcommons.org/croissant/column",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Extract"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "containedIn": {
        "@id": "http://mlcommons.org/croissant/containedIn",
        "rdfs:domain": [
          {
            "@id": "http://mlcommons.org/croissant/FileObject"
          },
          {
            "@id": "http://mlcommons.org/croissant/FileSet"
          }
        ],
        "rdfs:range": [
          {
            "@id": "http://mlcommons.org/croissant/FileObject"
          },
          {
            "@id": "http://mlcommons.org/croissant/FileSet"
          }
        ]
      },
      "content": {
        "@id": "http://mlcommons.org/croissant/content",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Extract"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/ContentExtractionEnumeration"
        }
      },
      "data": {
        "@id": "http://mlcommons.org/croissant/data",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/RecordSet"
        },
        "rdfs:range": {
          "@id": "http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON"
        }
      },
      "dataType": {
        "@id": "http://mlcommons.org/croissant/dataType",
        "rdfs:domain": [
          {
            "@id": "http://mlcommons.org/croissant/Field"
          },
          {
            "@id": "http://mlcommons.org/croissant/RecordSet"
          }
        ],
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/DataType"
        }
      },
      "delimiter": {
        "@id": "http://mlcommons.org/croissant/delimiter",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Transform"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "equivalentProperty": {
        "@id": "http://mlcommons.org/croissant/equivalentProperty",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Field"
        },
        "rdfs:range": {
          "@id": "https://schema.org/URL"
        }
      },
      "examples": {
        "@id": "http://mlcommons.org/croissant/examples",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/RecordSet"
        },
        "rdfs:range": {
          "@id": "http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON"
        }
      },
      "excludes": {
        "@id": "http://mlcommons.org/croissant/excludes",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/FileSet"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "extract": {
        "@id": "http://mlcommons.org/croissant/extract",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Extract"
        }
      },
      "field": {
        "@id": "http://mlcommons.org/croissant/field",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/RecordSet"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Field"
        }
      },
      "fileObject": {
        "@id": "http://mlcommons.org/croissant/fileObject",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/FileObject"
        }
      },
      "fileProperty": {
        "@id": "http://mlcommons.org/croissant/fileProperty",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Extract"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/FilePropertyEnumeration"
        }
      },
      "fileSet": {
        "@id": "http://mlcommons.org/croissant/fileSet",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/FileSet"
        }
      },
      "format": {
        "@id": "http://mlcommons.org/croissant/format",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Format"
        }
      },
      "includes": {
        "@id": "http://mlcommons.org/croissant/includes",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/FileSet"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "isLiveDataset": {
        "@id": "http://mlcommons.org/croissant/isLiveDataset",
        "rdfs:domain": {
          "@id": "https://schema.org/Dataset"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Boolean"
        }
      },
      "jsonPath": {
        "@id": "http://mlcommons.org/croissant/jsonPath",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Extract"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "jsonQuery": {
        "@id": "http://mlcommons.org/croissant/jsonQuery",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Transform"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "key": {
        "@id": "http://mlcommons.org/croissant/key",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/RecordSet"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Field"
        }
      },
      "parentField": {
        "@id": "http://mlcommons.org/croissant/parentField",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Field"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Field"
        }
      },
      "recordSet": {
        "@id": "http://mlcommons.org/croissant/recordSet",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/RecordSet"
        }
      },
      "references": {
        "@id": "http://mlcommons.org/croissant/references",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Field"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Field"
        }
      },
      "regex": {
        "@id": "http://mlcommons.org/croissant/regex",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Transform"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Text"
        }
      },
      "repeated": {
        "@id": "http://mlcommons.org/croissant/repeated",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Field"
        },
        "rdfs:range": {
          "@id": "https://schema.org/Boolean"
        }
      },
      "source": {
        "@id": "http://mlcommons.org/croissant/source",
        "rdfs:domain": [
          {
            "@id": "http://mlcommons.org/croissant/Field"
          },
          {
            "@id": "http://mlcommons.org/croissant/RecordSet"
          }
        ],
        "rdfs:range": [
          {
            "@id": "http://mlcommons.org/croissant/RecordSet"
          },
          {
            "@id": "http://mlcommons.org/croissant/FileObject"
          },
          {
            "@id": "http://mlcommons.org/croissant/DataSource"
          },
          {
            "@id": "http://mlcommons.org/croissant/FileSet"
          }
        ]
      },
      "subField": {
        "@id": "http://mlcommons.org/croissant/subField",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/Field"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Field"
        }
      },
      "transform": {
        "@id": "http://mlcommons.org/croissant/transform",
        "rdfs:domain": {
          "@id": "http://mlcommons.org/croissant/DataSource"
        },
        "rdfs:range": {
          "@id": "http://mlcommons.org/croissant/Transform"
        }
      }
    }
  }
---

# Vocabulary

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

---

### DataType

**URI:** `http://mlcommons.org/croissant/DataType`

**Description:** The data type of values expected for a Field in a RecordSet. This class is inspired by the Datatype class in CSVW. In addition to simple atomic types, types can be semantic types, such as schema.org classes, as well types defined in other vocabularies.

**Subclass of:**
- [https://schema.org/URL](https://schema.org/URL)

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
- [source](#source) (→ RecordSet, FileObject, DataSource, FileSet)
- [subField](#subField) (→ Field)

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

---

### Format

**URI:** `http://mlcommons.org/croissant/Format`

**Description:** Specifies how to parse the format of the data from a string representation. For example, format may hold a date format string, a number format, or a bounding box format.

**Subclass of:**
- [https://schema.org/Text](https://schema.org/Text)

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
- [source](#source) (→ RecordSet, FileObject, DataSource, FileSet)

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
- [http://mlcommons.org/croissant/RecordSet](http://mlcommons.org/croissant/RecordSet)
- [http://mlcommons.org/croissant/FileObject](http://mlcommons.org/croissant/FileObject)
- [http://mlcommons.org/croissant/DataSource](http://mlcommons.org/croissant/DataSource)
- [http://mlcommons.org/croissant/FileSet](http://mlcommons.org/croissant/FileSet)

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


