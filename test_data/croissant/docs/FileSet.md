---
term: http://mlcommons.org/croissant/FileSet
---

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