---
term: http://mlcommons.org/croissant/FileObject
---

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