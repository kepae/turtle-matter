---
title: PROV Ontology
namespace: http://www.w3.org/ns/prov#
jsonld_context: |
  {
    "@context": {
      "@vocab": "http://www.w3.org/ns/prov#",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "owl": "http://www.w3.org/2002/07/owl#",
      "Accept": {
        "@id": "http://www.w3.org/ns/prov#Accept",
        "@type": "@id"
      },
      "Activity": {
        "@id": "http://www.w3.org/ns/prov#Activity",
        "@type": "@id"
      },
      "ActivityInfluence": {
        "@id": "http://www.w3.org/ns/prov#ActivityInfluence",
        "@type": "@id"
      },
      "Agent": {
        "@id": "http://www.w3.org/ns/prov#Agent",
        "@type": "@id"
      },
      "AgentInfluence": {
        "@id": "http://www.w3.org/ns/prov#AgentInfluence",
        "@type": "@id"
      },
      "Association": {
        "@id": "http://www.w3.org/ns/prov#Association",
        "@type": "@id"
      },
      "Attribution": {
        "@id": "http://www.w3.org/ns/prov#Attribution",
        "@type": "@id"
      },
      "Bundle": {
        "@id": "http://www.w3.org/ns/prov#Bundle",
        "@type": "@id"
      },
      "Collection": {
        "@id": "http://www.w3.org/ns/prov#Collection",
        "@type": "@id"
      },
      "Communication": {
        "@id": "http://www.w3.org/ns/prov#Communication",
        "@type": "@id"
      },
      "Contribute": {
        "@id": "http://www.w3.org/ns/prov#Contribute",
        "@type": "@id"
      },
      "Contributor": {
        "@id": "http://www.w3.org/ns/prov#Contributor",
        "@type": "@id"
      },
      "Copyright": {
        "@id": "http://www.w3.org/ns/prov#Copyright",
        "@type": "@id"
      },
      "Create": {
        "@id": "http://www.w3.org/ns/prov#Create",
        "@type": "@id"
      },
      "Creator": {
        "@id": "http://www.w3.org/ns/prov#Creator",
        "@type": "@id"
      },
      "Delegation": {
        "@id": "http://www.w3.org/ns/prov#Delegation",
        "@type": "@id"
      },
      "Derivation": {
        "@id": "http://www.w3.org/ns/prov#Derivation",
        "@type": "@id"
      },
      "Dictionary": {
        "@id": "http://www.w3.org/ns/prov#Dictionary",
        "@type": "@id"
      },
      "DirectQueryService": {
        "@id": "http://www.w3.org/ns/prov#DirectQueryService",
        "@type": "@id"
      },
      "EmptyCollection": {
        "@id": "http://www.w3.org/ns/prov#EmptyCollection",
        "@type": "@id"
      },
      "EmptyDictionary": {
        "@id": "http://www.w3.org/ns/prov#EmptyDictionary",
        "@type": "@id"
      },
      "End": {
        "@id": "http://www.w3.org/ns/prov#End",
        "@type": "@id"
      },
      "Entity": {
        "@id": "http://www.w3.org/ns/prov#Entity",
        "@type": "@id"
      },
      "EntityInfluence": {
        "@id": "http://www.w3.org/ns/prov#EntityInfluence",
        "@type": "@id"
      },
      "Generation": {
        "@id": "http://www.w3.org/ns/prov#Generation",
        "@type": "@id"
      },
      "Influence": {
        "@id": "http://www.w3.org/ns/prov#Influence",
        "@type": "@id"
      },
      "Insertion": {
        "@id": "http://www.w3.org/ns/prov#Insertion",
        "@type": "@id"
      },
      "InstantaneousEvent": {
        "@id": "http://www.w3.org/ns/prov#InstantaneousEvent",
        "@type": "@id"
      },
      "Invalidation": {
        "@id": "http://www.w3.org/ns/prov#Invalidation",
        "@type": "@id"
      },
      "KeyEntityPair": {
        "@id": "http://www.w3.org/ns/prov#KeyEntityPair",
        "@type": "@id"
      },
      "Location": {
        "@id": "http://www.w3.org/ns/prov#Location",
        "@type": "@id"
      },
      "Modify": {
        "@id": "http://www.w3.org/ns/prov#Modify",
        "@type": "@id"
      },
      "Organization": {
        "@id": "http://www.w3.org/ns/prov#Organization",
        "@type": "@id"
      },
      "Person": {
        "@id": "http://www.w3.org/ns/prov#Person",
        "@type": "@id"
      },
      "Plan": {
        "@id": "http://www.w3.org/ns/prov#Plan",
        "@type": "@id"
      },
      "PrimarySource": {
        "@id": "http://www.w3.org/ns/prov#PrimarySource",
        "@type": "@id"
      },
      "Publish": {
        "@id": "http://www.w3.org/ns/prov#Publish",
        "@type": "@id"
      },
      "Publisher": {
        "@id": "http://www.w3.org/ns/prov#Publisher",
        "@type": "@id"
      },
      "Quotation": {
        "@id": "http://www.w3.org/ns/prov#Quotation",
        "@type": "@id"
      },
      "Removal": {
        "@id": "http://www.w3.org/ns/prov#Removal",
        "@type": "@id"
      },
      "Replace": {
        "@id": "http://www.w3.org/ns/prov#Replace",
        "@type": "@id"
      },
      "Revision": {
        "@id": "http://www.w3.org/ns/prov#Revision",
        "@type": "@id"
      },
      "RightsAssignment": {
        "@id": "http://www.w3.org/ns/prov#RightsAssignment",
        "@type": "@id"
      },
      "RightsHolder": {
        "@id": "http://www.w3.org/ns/prov#RightsHolder",
        "@type": "@id"
      },
      "Role": {
        "@id": "http://www.w3.org/ns/prov#Role",
        "@type": "@id"
      },
      "ServiceDescription": {
        "@id": "http://www.w3.org/ns/prov#ServiceDescription",
        "@type": "@id"
      },
      "SoftwareAgent": {
        "@id": "http://www.w3.org/ns/prov#SoftwareAgent",
        "@type": "@id"
      },
      "Start": {
        "@id": "http://www.w3.org/ns/prov#Start",
        "@type": "@id"
      },
      "Submit": {
        "@id": "http://www.w3.org/ns/prov#Submit",
        "@type": "@id"
      },
      "Usage": {
        "@id": "http://www.w3.org/ns/prov#Usage",
        "@type": "@id"
      },
      "actedOnBehalfOf": {
        "@id": "http://www.w3.org/ns/prov#actedOnBehalfOf"
      },
      "activity": {
        "@id": "http://www.w3.org/ns/prov#activity"
      },
      "agent": {
        "@id": "http://www.w3.org/ns/prov#agent"
      },
      "alternateOf": {
        "@id": "http://www.w3.org/ns/prov#alternateOf"
      },
      "asInBundle": {
        "@id": "http://www.w3.org/ns/prov#asInBundle"
      },
      "atLocation": {
        "@id": "http://www.w3.org/ns/prov#atLocation"
      },
      "atTime": {
        "@id": "http://www.w3.org/ns/prov#atTime"
      },
      "derivedByInsertionFrom": {
        "@id": "http://www.w3.org/ns/prov#derivedByInsertionFrom"
      },
      "derivedByRemovalFrom": {
        "@id": "http://www.w3.org/ns/prov#derivedByRemovalFrom"
      },
      "describesService": {
        "@id": "http://www.w3.org/ns/prov#describesService"
      },
      "dictionary": {
        "@id": "http://www.w3.org/ns/prov#dictionary"
      },
      "endedAtTime": {
        "@id": "http://www.w3.org/ns/prov#endedAtTime"
      },
      "entity": {
        "@id": "http://www.w3.org/ns/prov#entity"
      },
      "generated": {
        "@id": "http://www.w3.org/ns/prov#generated"
      },
      "generatedAtTime": {
        "@id": "http://www.w3.org/ns/prov#generatedAtTime"
      },
      "hadActivity": {
        "@id": "http://www.w3.org/ns/prov#hadActivity"
      },
      "hadDictionaryMember": {
        "@id": "http://www.w3.org/ns/prov#hadDictionaryMember"
      },
      "hadGeneration": {
        "@id": "http://www.w3.org/ns/prov#hadGeneration"
      },
      "hadMember": {
        "@id": "http://www.w3.org/ns/prov#hadMember"
      },
      "hadPlan": {
        "@id": "http://www.w3.org/ns/prov#hadPlan"
      },
      "hadPrimarySource": {
        "@id": "http://www.w3.org/ns/prov#hadPrimarySource"
      },
      "hadRole": {
        "@id": "http://www.w3.org/ns/prov#hadRole"
      },
      "hadUsage": {
        "@id": "http://www.w3.org/ns/prov#hadUsage"
      },
      "has_anchor": {
        "@id": "http://www.w3.org/ns/prov#has_anchor"
      },
      "has_provenance": {
        "@id": "http://www.w3.org/ns/prov#has_provenance"
      },
      "has_query_service": {
        "@id": "http://www.w3.org/ns/prov#has_query_service"
      },
      "influenced": {
        "@id": "http://www.w3.org/ns/prov#influenced"
      },
      "influencer": {
        "@id": "http://www.w3.org/ns/prov#influencer"
      },
      "insertedKeyEntityPair": {
        "@id": "http://www.w3.org/ns/prov#insertedKeyEntityPair"
      },
      "invalidated": {
        "@id": "http://www.w3.org/ns/prov#invalidated"
      },
      "invalidatedAtTime": {
        "@id": "http://www.w3.org/ns/prov#invalidatedAtTime"
      },
      "mentionOf": {
        "@id": "http://www.w3.org/ns/prov#mentionOf"
      },
      "pairEntity": {
        "@id": "http://www.w3.org/ns/prov#pairEntity"
      },
      "pairKey": {
        "@id": "http://www.w3.org/ns/prov#pairKey"
      },
      "pingback": {
        "@id": "http://www.w3.org/ns/prov#pingback"
      },
      "provenanceUriTemplate": {
        "@id": "http://www.w3.org/ns/prov#provenanceUriTemplate"
      },
      "qualifiedAssociation": {
        "@id": "http://www.w3.org/ns/prov#qualifiedAssociation"
      },
      "qualifiedAttribution": {
        "@id": "http://www.w3.org/ns/prov#qualifiedAttribution"
      },
      "qualifiedCommunication": {
        "@id": "http://www.w3.org/ns/prov#qualifiedCommunication"
      },
      "qualifiedDelegation": {
        "@id": "http://www.w3.org/ns/prov#qualifiedDelegation"
      },
      "qualifiedDerivation": {
        "@id": "http://www.w3.org/ns/prov#qualifiedDerivation"
      },
      "qualifiedEnd": {
        "@id": "http://www.w3.org/ns/prov#qualifiedEnd"
      },
      "qualifiedGeneration": {
        "@id": "http://www.w3.org/ns/prov#qualifiedGeneration"
      },
      "qualifiedInfluence": {
        "@id": "http://www.w3.org/ns/prov#qualifiedInfluence"
      },
      "qualifiedInsertion": {
        "@id": "http://www.w3.org/ns/prov#qualifiedInsertion"
      },
      "qualifiedInvalidation": {
        "@id": "http://www.w3.org/ns/prov#qualifiedInvalidation"
      },
      "qualifiedPrimarySource": {
        "@id": "http://www.w3.org/ns/prov#qualifiedPrimarySource"
      },
      "qualifiedQuotation": {
        "@id": "http://www.w3.org/ns/prov#qualifiedQuotation"
      },
      "qualifiedRemoval": {
        "@id": "http://www.w3.org/ns/prov#qualifiedRemoval"
      },
      "qualifiedRevision": {
        "@id": "http://www.w3.org/ns/prov#qualifiedRevision"
      },
      "qualifiedStart": {
        "@id": "http://www.w3.org/ns/prov#qualifiedStart"
      },
      "qualifiedUsage": {
        "@id": "http://www.w3.org/ns/prov#qualifiedUsage"
      },
      "removedKey": {
        "@id": "http://www.w3.org/ns/prov#removedKey"
      },
      "specializationOf": {
        "@id": "http://www.w3.org/ns/prov#specializationOf"
      },
      "startedAtTime": {
        "@id": "http://www.w3.org/ns/prov#startedAtTime"
      },
      "used": {
        "@id": "http://www.w3.org/ns/prov#used"
      },
      "value": {
        "@id": "http://www.w3.org/ns/prov#value"
      },
      "wasAssociatedWith": {
        "@id": "http://www.w3.org/ns/prov#wasAssociatedWith"
      },
      "wasAttributedTo": {
        "@id": "http://www.w3.org/ns/prov#wasAttributedTo"
      },
      "wasDerivedFrom": {
        "@id": "http://www.w3.org/ns/prov#wasDerivedFrom"
      },
      "wasEndedBy": {
        "@id": "http://www.w3.org/ns/prov#wasEndedBy"
      },
      "wasGeneratedBy": {
        "@id": "http://www.w3.org/ns/prov#wasGeneratedBy"
      },
      "wasInfluencedBy": {
        "@id": "http://www.w3.org/ns/prov#wasInfluencedBy"
      },
      "wasInformedBy": {
        "@id": "http://www.w3.org/ns/prov#wasInformedBy"
      },
      "wasInvalidatedBy": {
        "@id": "http://www.w3.org/ns/prov#wasInvalidatedBy"
      },
      "wasQuotedFrom": {
        "@id": "http://www.w3.org/ns/prov#wasQuotedFrom"
      },
      "wasRevisionOf": {
        "@id": "http://www.w3.org/ns/prov#wasRevisionOf"
      },
      "wasStartedBy": {
        "@id": "http://www.w3.org/ns/prov#wasStartedBy"
      }
    }
  }
---

# PROV Ontology

**Namespace:** http://www.w3.org/ns/prov#

## Classes (50)

### Accept

**URI:** `http://www.w3.org/ns/prov#Accept`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Activity

**URI:** `http://www.w3.org/ns/prov#Activity`

**Properties:**
- [endedAtTime](#endedAtTime) (→ XMLSchema#dateTime)
- [generated](#generated) (→ prov#Entity)
- [invalidated](#invalidated) (→ prov#Entity)
- [qualifiedAssociation](#qualifiedAssociation) (→ prov#Association)
- [qualifiedCommunication](#qualifiedCommunication) (→ prov#Communication)
- [qualifiedEnd](#qualifiedEnd) (→ prov#End)
- [qualifiedStart](#qualifiedStart) (→ prov#Start)
- [qualifiedUsage](#qualifiedUsage) (→ prov#Usage)
- [startedAtTime](#startedAtTime) (→ XMLSchema#dateTime)
- [used](#used) (→ prov#Entity)
- [wasAssociatedWith](#wasAssociatedWith) (→ prov#Agent)
- [wasEndedBy](#wasEndedBy) (→ prov#Entity)
- [wasInformedBy](#wasInformedBy) (→ prov#Activity)
- [wasStartedBy](#wasStartedBy) (→ prov#Entity)

---

### ActivityInfluence

**URI:** `http://www.w3.org/ns/prov#ActivityInfluence`

**Description:** ActivityInfluence provides additional descriptions of an Activity's binary influence upon any other kind of resource. Instances of ActivityInfluence use the prov:activity property to cite the influencing Activity.

**Subclass of:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)
- [n1f22c49a9de04e33a970d2b6d116d86ab1](n1f22c49a9de04e33a970d2b6d116d86ab1)

**Properties:**
- [activity](#activity) (→ prov#Activity)

---

### Agent

**URI:** `http://www.w3.org/ns/prov#Agent`

**Properties:**
- [actedOnBehalfOf](#actedOnBehalfOf) (→ prov#Agent)
- [qualifiedDelegation](#qualifiedDelegation) (→ prov#Delegation)

---

### AgentInfluence

**URI:** `http://www.w3.org/ns/prov#AgentInfluence`

**Description:** AgentInfluence provides additional descriptions of an Agent's binary influence upon any other kind of resource. Instances of AgentInfluence use the prov:agent property to cite the influencing Agent.

**Subclass of:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)

**Properties:**
- [agent](#agent) (→ prov#Agent)

---

### Association

**URI:** `http://www.w3.org/ns/prov#Association`

**Description:** An instance of prov:Association provides additional descriptions about the binary prov:wasAssociatedWith relation from an prov:Activity to some prov:Agent that had some responsiblity for it. For example, :baking prov:wasAssociatedWith :baker; prov:qualifiedAssociation [ a prov:Association; prov:agent :baker; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#AgentInfluence](http://www.w3.org/ns/prov#AgentInfluence)

**Properties:**
- [hadPlan](#hadPlan) (→ prov#Plan)

---

### Attribution

**URI:** `http://www.w3.org/ns/prov#Attribution`

**Description:** An instance of prov:Attribution provides additional descriptions about the binary prov:wasAttributedTo relation from an prov:Entity to some prov:Agent that had some responsible for it. For example, :cake prov:wasAttributedTo :baker; prov:qualifiedAttribution [ a prov:Attribution; prov:entity :baker; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#AgentInfluence](http://www.w3.org/ns/prov#AgentInfluence)

---

### Bundle

**URI:** `http://www.w3.org/ns/prov#Bundle`

**Description:** Note that there are kinds of bundles (e.g. handwritten letters, audio recordings, etc.) that are not expressed in PROV-O, but can be still be described by PROV-O.

**Subclass of:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### Collection

**URI:** `http://www.w3.org/ns/prov#Collection`

**Subclass of:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Properties:**
- [hadMember](#hadMember) (→ prov#Entity)

---

### Communication

**URI:** `http://www.w3.org/ns/prov#Communication`

**Description:** An instance of prov:Communication provides additional descriptions about the binary prov:wasInformedBy relation from an informed prov:Activity to the prov:Activity that informed it. For example, :you_jumping_off_bridge prov:wasInformedBy :everyone_else_jumping_off_bridge; prov:qualifiedCommunication [ a prov:Communication; prov:activity :everyone_else_jumping_off_bridge; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#ActivityInfluence](http://www.w3.org/ns/prov#ActivityInfluence)

---

### Contribute


**URI:** `http://www.w3.org/ns/prov#Contribute`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Contributor

**URI:** `http://www.w3.org/ns/prov#Contributor`

**Subclass of:**
- [http://www.w3.org/ns/prov#Role](http://www.w3.org/ns/prov#Role)

---

### Copyright

**URI:** `http://www.w3.org/ns/prov#Copyright`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Create

**URI:** `http://www.w3.org/ns/prov#Create`

**Subclass of:**
- [http://www.w3.org/ns/prov#Contribute](http://www.w3.org/ns/prov#Contribute)

---

### Creator

**URI:** `http://www.w3.org/ns/prov#Creator`

**Subclass of:**
- [http://www.w3.org/ns/prov#Contributor](http://www.w3.org/ns/prov#Contributor)

---

### Delegation

**URI:** `http://www.w3.org/ns/prov#Delegation`

**Description:** An instance of prov:Delegation provides additional descriptions about the binary prov:actedOnBehalfOf relation from a performing prov:Agent to some prov:Agent for whom it was performed. For example, :mixing prov:wasAssociatedWith :toddler . :toddler prov:actedOnBehalfOf :mother; prov:qualifiedDelegation [ a prov:Delegation; prov:entity :mother; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#AgentInfluence](http://www.w3.org/ns/prov#AgentInfluence)

---

### Derivation

**URI:** `http://www.w3.org/ns/prov#Derivation`

**Description:** An instance of prov:Derivation provides additional descriptions about the binary prov:wasDerivedFrom relation from some derived prov:Entity to another prov:Entity from which it was derived. For example, :chewed_bubble_gum prov:wasDerivedFrom :unwrapped_bubble_gum; prov:qualifiedDerivation [ a prov:Derivation; prov:entity :unwrapped_bubble_gum; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#EntityInfluence](http://www.w3.org/ns/prov#EntityInfluence)

**Properties:**
- [hadGeneration](#hadGeneration) (→ prov#Generation)
- [hadUsage](#hadUsage) (→ prov#Usage)

---

### Dictionary

**URI:** `http://www.w3.org/ns/prov#Dictionary`

**Description:** This concept allows for the provenance of the dictionary, but also of its constituents to be expressed. Such a notion of dictionary corresponds to a wide variety of concrete data structures, such as a maps or associative arrays.

**Properties:**
- [derivedByInsertionFrom](#derivedByInsertionFrom) (→ prov#Dictionary)
- [derivedByRemovalFrom](#derivedByRemovalFrom) (→ prov#Dictionary)
- [hadDictionaryMember](#hadDictionaryMember) (→ prov#KeyEntityPair)
- [qualifiedInsertion](#qualifiedInsertion) (→ prov#Insertion)
- [qualifiedRemoval](#qualifiedRemoval) (→ prov#Removal)

---

### ProvenanceService

**URI:** `http://www.w3.org/ns/prov#DirectQueryService`

**Description:** Type for a generic provenance query service. Mainly for use in RDF provenance query service descriptions, to facilitate discovery in linked data environments.

**Subclass of:**
- [http://www.w3.org/ns/prov#SoftwareAgent](http://www.w3.org/ns/prov#SoftwareAgent)

---

### EmptyCollection

**URI:** `http://www.w3.org/ns/prov#EmptyCollection`

**Subclass of:**
- [http://www.w3.org/ns/prov#Collection](http://www.w3.org/ns/prov#Collection)

---

### Empty Dictionary

**URI:** `http://www.w3.org/ns/prov#EmptyDictionary`

**Subclass of:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)
- [http://www.w3.org/ns/prov#EmptyCollection](http://www.w3.org/ns/prov#EmptyCollection)

---

### End

**URI:** `http://www.w3.org/ns/prov#End`

**Description:** An instance of prov:End provides additional descriptions about the binary prov:wasEndedBy relation from some ended prov:Activity to an prov:Entity that ended it. For example, :ball_game prov:wasEndedBy :buzzer; prov:qualifiedEnd [ a prov:End; prov:entity :buzzer; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ].

**Subclass of:**
- [http://www.w3.org/ns/prov#EntityInfluence](http://www.w3.org/ns/prov#EntityInfluence)
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

---

### Entity

**URI:** `http://www.w3.org/ns/prov#Entity`

**Properties:**
- [alternateOf](#alternateOf) (→ prov#Entity)
- [asInBundle](#asInBundle) (→ prov#Bundle)
- [generatedAtTime](#generatedAtTime) (→ XMLSchema#dateTime)
- [hadPrimarySource](#hadPrimarySource) (→ prov#Entity)
- [invalidatedAtTime](#invalidatedAtTime) (→ XMLSchema#dateTime)
- [mentionOf](#mentionOf) (→ prov#Entity)
- [qualifiedAttribution](#qualifiedAttribution) (→ prov#Attribution)
- [qualifiedDerivation](#qualifiedDerivation) (→ prov#Derivation)
- [qualifiedGeneration](#qualifiedGeneration) (→ prov#Generation)
- [qualifiedInvalidation](#qualifiedInvalidation) (→ prov#Invalidation)
- [qualifiedPrimarySource](#qualifiedPrimarySource) (→ prov#PrimarySource)
- [qualifiedQuotation](#qualifiedQuotation) (→ prov#Quotation)
- [qualifiedRevision](#qualifiedRevision) (→ prov#Revision)
- [specializationOf](#specializationOf) (→ prov#Entity)
- [value](#value)
- [wasAttributedTo](#wasAttributedTo) (→ prov#Agent)
- [wasDerivedFrom](#wasDerivedFrom) (→ prov#Entity)
- [wasGeneratedBy](#wasGeneratedBy) (→ prov#Activity)
- [wasInvalidatedBy](#wasInvalidatedBy) (→ prov#Activity)
- [wasQuotedFrom](#wasQuotedFrom) (→ prov#Entity)
- [wasRevisionOf](#wasRevisionOf) (→ prov#Entity)

---

### EntityInfluence

**URI:** `http://www.w3.org/ns/prov#EntityInfluence`

**Description:** EntityInfluence provides additional descriptions of an Entity's binary influence upon any other kind of resource. Instances of EntityInfluence use the prov:entity property to cite the influencing Entity.

**Subclass of:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)

**Properties:**
- [entity](#entity) (→ prov#Entity)

---

### Generation

**URI:** `http://www.w3.org/ns/prov#Generation`

**Description:** An instance of prov:Generation provides additional descriptions about the binary prov:wasGeneratedBy relation from a generated prov:Entity to the prov:Activity that generated it. For example, :cake prov:wasGeneratedBy :baking; prov:qualifiedGeneration [ a prov:Generation; prov:activity :baking; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#ActivityInfluence](http://www.w3.org/ns/prov#ActivityInfluence)
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

---

### Influence

**URI:** `http://www.w3.org/ns/prov#Influence`

**Description:** An instance of prov:Influence provides additional descriptions about the binary prov:wasInfluencedBy relation from some influenced Activity, Entity, or Agent to the influencing Activity, Entity, or Agent. For example, :stomach_ache prov:wasInfluencedBy :spoon; prov:qualifiedInfluence [ a prov:Influence; prov:entity :spoon; :foo :bar ] . Because prov:Influence is a broad relation, the more specific relations (Communication, Delegation, End, etc.) should be used when applicable.

**Properties:**
- [hadActivity](#hadActivity) (→ prov#Activity)
- [hadRole](#hadRole) (→ prov#Role)
- [influencer](#influencer) (→ owl#Thing)

---

### Insertion

**URI:** `http://www.w3.org/ns/prov#Insertion`

**Subclass of:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)
- [n1f22c49a9de04e33a970d2b6d116d86ab71](n1f22c49a9de04e33a970d2b6d116d86ab71)
- [n1f22c49a9de04e33a970d2b6d116d86ab72](n1f22c49a9de04e33a970d2b6d116d86ab72)

**Properties:**
- [dictionary](#dictionary) (→ prov#Dictionary)
- [insertedKeyEntityPair](#insertedKeyEntityPair) (→ prov#KeyEntityPair)

---

### InstantaneousEvent

**URI:** `http://www.w3.org/ns/prov#InstantaneousEvent`

**Description:** An instantaneous event, or event for short, happens in the world and marks a change in the world, in its activities and in its entities. The term 'event' is commonly used in process algebra with a similar meaning. Events represent communications or interactions; they are assumed to be atomic and instantaneous.

**Properties:**
- [atTime](#atTime) (→ XMLSchema#dateTime)

---

### Invalidation

**URI:** `http://www.w3.org/ns/prov#Invalidation`

**Description:** An instance of prov:Invalidation provides additional descriptions about the binary prov:wasInvalidatedBy relation from an invalidated prov:Entity to the prov:Activity that invalidated it. For example, :uncracked_egg prov:wasInvalidatedBy :baking; prov:qualifiedInvalidation [ a prov:Invalidation; prov:activity :baking; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#ActivityInfluence](http://www.w3.org/ns/prov#ActivityInfluence)
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

---

### Key-Entity Pair

**URI:** `http://www.w3.org/ns/prov#KeyEntityPair`

**Subclass of:**
- [n1f22c49a9de04e33a970d2b6d116d86ab69](n1f22c49a9de04e33a970d2b6d116d86ab69)
- [n1f22c49a9de04e33a970d2b6d116d86ab70](n1f22c49a9de04e33a970d2b6d116d86ab70)

**Properties:**
- [pairEntity](#pairEntity) (→ prov#Entity)
- [pairKey](#pairKey) (→ rdf-schema#Literal)

---

### Location

**URI:** `http://www.w3.org/ns/prov#Location`

---

### Modify

**URI:** `http://www.w3.org/ns/prov#Modify`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Organization

**URI:** `http://www.w3.org/ns/prov#Organization`

**Subclass of:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### Person

**URI:** `http://www.w3.org/ns/prov#Person`

**Subclass of:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### Plan

**URI:** `http://www.w3.org/ns/prov#Plan`

**Description:** There exist no prescriptive requirement on the nature of plans, their representation, the actions or steps they consist of, or their intended goals. Since plans may evolve over time, it may become necessary to track their provenance, so plans themselves are entities. Representing the plan explicitly in the provenance can be useful for various tasks: for example, to validate the execution as represented in the provenance record, to manage expectation failures, or to provide explanations.

**Subclass of:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### PrimarySource

**URI:** `http://www.w3.org/ns/prov#PrimarySource`

**Description:** An instance of prov:PrimarySource provides additional descriptions about the binary prov:hadPrimarySource relation from some secondary prov:Entity to an earlier, primary prov:Entity. For example, :blog prov:hadPrimarySource :newsArticle; prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :newsArticle; :foo :bar ] .

**Subclass of:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

---

### Publish

**URI:** `http://www.w3.org/ns/prov#Publish`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Publisher

**URI:** `http://www.w3.org/ns/prov#Publisher`

**Subclass of:**
- [http://www.w3.org/ns/prov#Role](http://www.w3.org/ns/prov#Role)

---

### Quotation

**URI:** `http://www.w3.org/ns/prov#Quotation`

**Description:** An instance of prov:Quotation provides additional descriptions about the binary prov:wasQuotedFrom relation from some taken prov:Entity from an earlier, larger prov:Entity. For example, :here_is_looking_at_you_kid prov:wasQuotedFrom :casablanca_script; prov:qualifiedQuotation [ a prov:Quotation; prov:entity :casablanca_script; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

---

### Removal

**URI:** `http://www.w3.org/ns/prov#Removal`

**Subclass of:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)
- [n1f22c49a9de04e33a970d2b6d116d86ab73](n1f22c49a9de04e33a970d2b6d116d86ab73)
- [n1f22c49a9de04e33a970d2b6d116d86ab74](n1f22c49a9de04e33a970d2b6d116d86ab74)

**Properties:**
- [dictionary](#dictionary) (→ prov#Dictionary)
- [removedKey](#removedKey) (→ rdf-schema#Literal)

---

### Replace

**URI:** `http://www.w3.org/ns/prov#Replace`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Revision

**URI:** `http://www.w3.org/ns/prov#Revision`

**Description:** An instance of prov:Revision provides additional descriptions about the binary prov:wasRevisionOf relation from some newer prov:Entity to an earlier prov:Entity. For example, :draft_2 prov:wasRevisionOf :draft_1; prov:qualifiedRevision [ a prov:Revision; prov:entity :draft_1; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

---

### RightsAssignment

**URI:** `http://www.w3.org/ns/prov#RightsAssignment`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### RightsHolder

**URI:** `http://www.w3.org/ns/prov#RightsHolder`

**Subclass of:**
- [http://www.w3.org/ns/prov#Role](http://www.w3.org/ns/prov#Role)

---

### Role

**URI:** `http://www.w3.org/ns/prov#Role`

---

### ServiceDescription

**URI:** `http://www.w3.org/ns/prov#ServiceDescription`

**Description:** Type for a generic provenance query service. Mainly for use in RDF provenance query service descriptions, to facilitate discovery in linked data environments.

**Subclass of:**
- [http://www.w3.org/ns/prov#SoftwareAgent](http://www.w3.org/ns/prov#SoftwareAgent)

---

### SoftwareAgent

**URI:** `http://www.w3.org/ns/prov#SoftwareAgent`

**Subclass of:**
- [http://www.w3.org/2002/07/owl#Thing](http://www.w3.org/2002/07/owl#Thing)
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### Start

**URI:** `http://www.w3.org/ns/prov#Start`

**Description:** An instance of prov:Start provides additional descriptions about the binary prov:wasStartedBy relation from some started prov:Activity to an prov:Entity that started it. For example, :foot_race prov:wasStartedBy :bang; prov:qualifiedStart [ a prov:Start; prov:entity :bang; :foo :bar; prov:atTime '2012-03-09T08:05:08-05:00'^^xsd:dateTime ] .

**Subclass of:**
- [http://www.w3.org/ns/prov#EntityInfluence](http://www.w3.org/ns/prov#EntityInfluence)
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

---

### Submit

**URI:** `http://www.w3.org/ns/prov#Submit`

**Subclass of:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### Usage

**URI:** `http://www.w3.org/ns/prov#Usage`

**Description:** An instance of prov:Usage provides additional descriptions about the binary prov:used relation from some prov:Activity to an prov:Entity that it used. For example, :keynote prov:used :podium; prov:qualifiedUsage [ a prov:Usage; prov:entity :podium; :foo :bar ].

**Subclass of:**
- [http://www.w3.org/ns/prov#EntityInfluence](http://www.w3.org/ns/prov#EntityInfluence)
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

---

## Properties (68)

### actedOnBehalfOf

**URI:** `http://www.w3.org/ns/prov#actedOnBehalfOf`

**Description:** An object property to express the accountability of an agent towards another agent. The subordinate agent acted on behalf of the responsible agent in an actual activity. 

**Domain:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

**Range:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### activity

**URI:** `http://www.w3.org/ns/prov#activity`

**Domain:**
- [http://www.w3.org/ns/prov#ActivityInfluence](http://www.w3.org/ns/prov#ActivityInfluence)

**Range:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### agent

**URI:** `http://www.w3.org/ns/prov#agent`

**Domain:**
- [http://www.w3.org/ns/prov#AgentInfluence](http://www.w3.org/ns/prov#AgentInfluence)

**Range:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### alternateOf

**URI:** `http://www.w3.org/ns/prov#alternateOf`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### asInBundle

**URI:** `http://www.w3.org/ns/prov#asInBundle`

**Description:** prov:asInBundle is used to specify which bundle the general entity of a prov:mentionOf property is described.

When :x prov:mentionOf :y and :y is described in Bundle :b, the triple :x prov:asInBundle :b is also asserted to cite the Bundle in which :y was described.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Bundle](http://www.w3.org/ns/prov#Bundle)

---

### atLocation

**URI:** `http://www.w3.org/ns/prov#atLocation`

**Description:** The Location of any resource.

**Domain:**
- [n1f22c49a9de04e33a970d2b6d116d86ab4](n1f22c49a9de04e33a970d2b6d116d86ab4)

**Range:**
- [http://www.w3.org/ns/prov#Location](http://www.w3.org/ns/prov#Location)

---

### atTime

**URI:** `http://www.w3.org/ns/prov#atTime`

**Description:** The time at which an InstantaneousEvent occurred, in the form of xsd:dateTime.

**Domain:**
- [http://www.w3.org/ns/prov#InstantaneousEvent](http://www.w3.org/ns/prov#InstantaneousEvent)

**Range:**
- [http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

---

### derivedByInsertionFrom

**URI:** `http://www.w3.org/ns/prov#derivedByInsertionFrom`

**Domain:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

**Range:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

---

### derivedByRemovalFrom

**URI:** `http://www.w3.org/ns/prov#derivedByRemovalFrom`

**Domain:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

**Range:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

---

### describesService

**URI:** `http://www.w3.org/ns/prov#describesService`

**Description:** relates a generic provenance query service resource (type prov:ServiceDescription) to a specific query service description (e.g. a prov:DirectQueryService or a sd:Service).

---

### dictionary

**URI:** `http://www.w3.org/ns/prov#dictionary`

**Domain:**
- [http://www.w3.org/ns/prov#Insertion](http://www.w3.org/ns/prov#Insertion)
- [http://www.w3.org/ns/prov#Removal](http://www.w3.org/ns/prov#Removal)

**Range:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

---

### endedAtTime

**URI:** `http://www.w3.org/ns/prov#endedAtTime`

**Description:** The time at which an activity ended. See also prov:startedAtTime.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

---

### entity

**URI:** `http://www.w3.org/ns/prov#entity`

**Domain:**
- [http://www.w3.org/ns/prov#EntityInfluence](http://www.w3.org/ns/prov#EntityInfluence)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### generated

**URI:** `http://www.w3.org/ns/prov#generated`

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### generatedAtTime

**URI:** `http://www.w3.org/ns/prov#generatedAtTime`

**Description:** The time at which an entity was completely created and is available for use.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

---

### hadActivity

**URI:** `http://www.w3.org/ns/prov#hadActivity`

**Description:** The _optional_ Activity of an Influence, which used, generated, invalidated, or was the responsibility of some Entity. This property is _not_ used by ActivityInfluence (use prov:activity instead).

**Domain:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)
- [n1f22c49a9de04e33a970d2b6d116d86ab9](n1f22c49a9de04e33a970d2b6d116d86ab9)

**Range:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### hadDictionaryMember

**URI:** `http://www.w3.org/ns/prov#hadDictionaryMember`

**Domain:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

**Range:**
- [http://www.w3.org/ns/prov#KeyEntityPair](http://www.w3.org/ns/prov#KeyEntityPair)

---

### hadGeneration

**URI:** `http://www.w3.org/ns/prov#hadGeneration`

**Description:** The _optional_ Generation involved in an Entity's Derivation.

**Domain:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

**Range:**
- [http://www.w3.org/ns/prov#Generation](http://www.w3.org/ns/prov#Generation)

---

### hadMember

**URI:** `http://www.w3.org/ns/prov#hadMember`

**Domain:**
- [http://www.w3.org/ns/prov#Collection](http://www.w3.org/ns/prov#Collection)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### hadPlan

**URI:** `http://www.w3.org/ns/prov#hadPlan`

**Description:** The _optional_ Plan adopted by an Agent in Association with some Activity. Plan specifications are out of the scope of this specification.

**Domain:**
- [http://www.w3.org/ns/prov#Association](http://www.w3.org/ns/prov#Association)

**Range:**
- [http://www.w3.org/ns/prov#Plan](http://www.w3.org/ns/prov#Plan)

---

### hadPrimarySource

**URI:** `http://www.w3.org/ns/prov#hadPrimarySource`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### hadRole

**URI:** `http://www.w3.org/ns/prov#hadRole`

**Description:** The _optional_ Role that an Entity assumed in the context of an Activity. For example, :baking prov:used :spoon; prov:qualified [ a prov:Usage; prov:entity :spoon; prov:hadRole roles:mixing_implement ].

**Domain:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)
- [n1f22c49a9de04e33a970d2b6d116d86ab16](n1f22c49a9de04e33a970d2b6d116d86ab16)

**Range:**
- [http://www.w3.org/ns/prov#Role](http://www.w3.org/ns/prov#Role)

---

### hadUsage

**URI:** `http://www.w3.org/ns/prov#hadUsage`

**Description:** The _optional_ Usage involved in an Entity's Derivation.

**Domain:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

**Range:**
- [http://www.w3.org/ns/prov#Usage](http://www.w3.org/ns/prov#Usage)

---

### has_anchor

**URI:** `http://www.w3.org/ns/prov#has_anchor`

**Description:** Indicates anchor URI for a potentially dynamic resource instance.

---

### has_provenance

**URI:** `http://www.w3.org/ns/prov#has_provenance`

**Description:** Indicates a provenance-URI for a resource; the resource identified by this property presents a provenance record about its subject or anchor resource.

---

### hasProvenanceService

**URI:** `http://www.w3.org/ns/prov#has_query_service`

**Description:** Indicates a provenance query service that can access provenance related to its subject or anchor resource.

---

### influenced

**URI:** `http://www.w3.org/ns/prov#influenced`

---

### influencer

**URI:** `http://www.w3.org/ns/prov#influencer`

**Description:** Subproperties of prov:influencer are used to cite the object of an unqualified PROV-O triple whose predicate is a subproperty of prov:wasInfluencedBy (e.g. prov:used, prov:wasGeneratedBy). prov:influencer is used much like rdf:object is used.

**Domain:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)

**Range:**
- [http://www.w3.org/2002/07/owl#Thing](http://www.w3.org/2002/07/owl#Thing)

---

### insertedKeyEntityPair

**URI:** `http://www.w3.org/ns/prov#insertedKeyEntityPair`

**Domain:**
- [http://www.w3.org/ns/prov#Insertion](http://www.w3.org/ns/prov#Insertion)

**Range:**
- [http://www.w3.org/ns/prov#KeyEntityPair](http://www.w3.org/ns/prov#KeyEntityPair)

---

### invalidated

**URI:** `http://www.w3.org/ns/prov#invalidated`

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### invalidatedAtTime

**URI:** `http://www.w3.org/ns/prov#invalidatedAtTime`

**Description:** The time at which an entity was invalidated (i.e., no longer usable).

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

---

### mentionOf

**URI:** `http://www.w3.org/ns/prov#mentionOf`

**Description:** prov:mentionOf is used to specialize an entity as described in another bundle. It is to be used in conjuction with prov:asInBundle.

prov:asInBundle is used to cite the Bundle in which the generalization was mentioned.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### pairKey

**URI:** `http://www.w3.org/ns/prov#pairEntity`

**Domain:**
- [http://www.w3.org/ns/prov#KeyEntityPair](http://www.w3.org/ns/prov#KeyEntityPair)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### pairKey

**URI:** `http://www.w3.org/ns/prov#pairKey`

**Domain:**
- [http://www.w3.org/ns/prov#KeyEntityPair](http://www.w3.org/ns/prov#KeyEntityPair)

**Range:**
- [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)

---

### provenance pingback

**URI:** `http://www.w3.org/ns/prov#pingback`

**Description:** Relates a resource to a provenance pingback service that may receive additional provenance links about the resource.

---

### provenanceUriTemplate

**URI:** `http://www.w3.org/ns/prov#provenanceUriTemplate`

**Description:** Relates a provenance service to a URI template string for constructing provenance-URIs.

---

### qualifiedAssociation

**URI:** `http://www.w3.org/ns/prov#qualifiedAssociation`

**Description:** If this Activity prov:wasAssociatedWith Agent :ag, then it can qualify the Association using prov:qualifiedAssociation [ a prov:Association;  prov:agent :ag; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Association](http://www.w3.org/ns/prov#Association)

---

### qualifiedAttribution

**URI:** `http://www.w3.org/ns/prov#qualifiedAttribution`

**Description:** If this Entity prov:wasAttributedTo Agent :ag, then it can qualify how it was influenced using prov:qualifiedAttribution [ a prov:Attribution;  prov:agent :ag; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Attribution](http://www.w3.org/ns/prov#Attribution)

---

### qualifiedCommunication

**URI:** `http://www.w3.org/ns/prov#qualifiedCommunication`

**Description:** If this Activity prov:wasInformedBy Activity :a, then it can qualify how it was influenced using prov:qualifiedCommunication [ a prov:Communication;  prov:activity :a; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Communication](http://www.w3.org/ns/prov#Communication)

---

### qualifiedDelegation

**URI:** `http://www.w3.org/ns/prov#qualifiedDelegation`

**Description:** If this Agent prov:actedOnBehalfOf Agent :ag, then it can qualify how with prov:qualifiedResponsibility [ a prov:Responsibility;  prov:agent :ag; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

**Range:**
- [http://www.w3.org/ns/prov#Delegation](http://www.w3.org/ns/prov#Delegation)

---

### qualifiedDerivation

**URI:** `http://www.w3.org/ns/prov#qualifiedDerivation`

**Description:** If this Entity prov:wasDerivedFrom Entity :e, then it can qualify how it was derived using prov:qualifiedDerivation [ a prov:Derivation;  prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Derivation](http://www.w3.org/ns/prov#Derivation)

---

### qualifiedEnd

**URI:** `http://www.w3.org/ns/prov#qualifiedEnd`

**Description:** If this Activity prov:wasEndedBy Entity :e1, then it can qualify how it was ended using prov:qualifiedEnd [ a prov:End;  prov:entity :e1; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#End](http://www.w3.org/ns/prov#End)

---

### qualifiedGeneration

**URI:** `http://www.w3.org/ns/prov#qualifiedGeneration`

**Description:** If this Activity prov:generated Entity :e, then it can qualify how it performed the Generation using prov:qualifiedGeneration [ a prov:Generation;  prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Generation](http://www.w3.org/ns/prov#Generation)

---

### qualifiedInfluence

**URI:** `http://www.w3.org/ns/prov#qualifiedInfluence`

**Description:** Because prov:qualifiedInfluence is a broad relation, the more specific relations (qualifiedCommunication, qualifiedDelegation, qualifiedEnd, etc.) should be used when applicable.

**Domain:**
- [n1f22c49a9de04e33a970d2b6d116d86ab19](n1f22c49a9de04e33a970d2b6d116d86ab19)

**Range:**
- [http://www.w3.org/ns/prov#Influence](http://www.w3.org/ns/prov#Influence)

---

### qualifiedInsertion

**URI:** `http://www.w3.org/ns/prov#qualifiedInsertion`

**Domain:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

**Range:**
- [http://www.w3.org/ns/prov#Insertion](http://www.w3.org/ns/prov#Insertion)

---

### qualifiedInvalidation

**URI:** `http://www.w3.org/ns/prov#qualifiedInvalidation`

**Description:** If this Entity prov:wasInvalidatedBy Activity :a, then it can qualify how it was invalidated using prov:qualifiedInvalidation [ a prov:Invalidation;  prov:activity :a; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Invalidation](http://www.w3.org/ns/prov#Invalidation)

---

### qualifiedPrimarySource

**URI:** `http://www.w3.org/ns/prov#qualifiedPrimarySource`

**Description:** If this Entity prov:hadPrimarySource Entity :e, then it can qualify how using prov:qualifiedPrimarySource [ a prov:PrimarySource; prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#PrimarySource](http://www.w3.org/ns/prov#PrimarySource)

---

### qualifiedQuotation

**URI:** `http://www.w3.org/ns/prov#qualifiedQuotation`

**Description:** If this Entity prov:wasQuotedFrom Entity :e, then it can qualify how using prov:qualifiedQuotation [ a prov:Quotation;  prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Quotation](http://www.w3.org/ns/prov#Quotation)

---

### qualifiedRemoval

**URI:** `http://www.w3.org/ns/prov#qualifiedRemoval`

**Domain:**
- [http://www.w3.org/ns/prov#Dictionary](http://www.w3.org/ns/prov#Dictionary)

**Range:**
- [http://www.w3.org/ns/prov#Removal](http://www.w3.org/ns/prov#Removal)

---

### qualifiedRevision

**URI:** `http://www.w3.org/ns/prov#qualifiedRevision`

**Description:** If this Entity prov:wasRevisionOf Entity :e, then it can qualify how it was revised using prov:qualifiedRevision [ a prov:Revision;  prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Revision](http://www.w3.org/ns/prov#Revision)

---

### qualifiedStart

**URI:** `http://www.w3.org/ns/prov#qualifiedStart`

**Description:** If this Activity prov:wasStartedBy Entity :e1, then it can qualify how it was started using prov:qualifiedStart [ a prov:Start;  prov:entity :e1; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Start](http://www.w3.org/ns/prov#Start)

---

### qualifiedUsage

**URI:** `http://www.w3.org/ns/prov#qualifiedUsage`

**Description:** If this Activity prov:used Entity :e, then it can qualify how it used it using prov:qualifiedUsage [ a prov:Usage; prov:entity :e; :foo :bar ].

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Usage](http://www.w3.org/ns/prov#Usage)

---

### removedKey

**URI:** `http://www.w3.org/ns/prov#removedKey`

**Domain:**
- [http://www.w3.org/ns/prov#Removal](http://www.w3.org/ns/prov#Removal)

**Range:**
- [http://www.w3.org/2000/01/rdf-schema#Literal](http://www.w3.org/2000/01/rdf-schema#Literal)

---

### specializationOf

**URI:** `http://www.w3.org/ns/prov#specializationOf`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### startedAtTime

**URI:** `http://www.w3.org/ns/prov#startedAtTime`

**Description:** The time at which an activity started. See also prov:endedAtTime.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/2001/XMLSchema#dateTime](http://www.w3.org/2001/XMLSchema#dateTime)

---

### used

**URI:** `http://www.w3.org/ns/prov#used`

**Description:** A prov:Entity that was used by this prov:Activity. For example, :baking prov:used :spoon, :egg, :oven .

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### value

**URI:** `http://www.w3.org/ns/prov#value`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### wasAssociatedWith

**URI:** `http://www.w3.org/ns/prov#wasAssociatedWith`

**Description:** An prov:Agent that had some (unspecified) responsibility for the occurrence of this prov:Activity.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### wasAttributedTo

**URI:** `http://www.w3.org/ns/prov#wasAttributedTo`

**Description:** Attribution is the ascribing of an entity to an agent.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Agent](http://www.w3.org/ns/prov#Agent)

---

### wasDerivedFrom

**URI:** `http://www.w3.org/ns/prov#wasDerivedFrom`

**Description:** The more specific subproperties of prov:wasDerivedFrom (i.e., prov:wasQuotedFrom, prov:wasRevisionOf, prov:hadPrimarySource) should be used when applicable.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### wasEndedBy

**URI:** `http://www.w3.org/ns/prov#wasEndedBy`

**Description:** End is when an activity is deemed to have ended. An end may refer to an entity, known as trigger, that terminated the activity.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### wasGeneratedBy

**URI:** `http://www.w3.org/ns/prov#wasGeneratedBy`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### wasInfluencedBy

**URI:** `http://www.w3.org/ns/prov#wasInfluencedBy`

**Description:** Because prov:wasInfluencedBy is a broad relation, its more specific subproperties (e.g. prov:wasInformedBy, prov:actedOnBehalfOf, prov:wasEndedBy, etc.) should be used when applicable.

**Domain:**
- [n1f22c49a9de04e33a970d2b6d116d86ab35](n1f22c49a9de04e33a970d2b6d116d86ab35)

**Range:**
- [n1f22c49a9de04e33a970d2b6d116d86ab39](n1f22c49a9de04e33a970d2b6d116d86ab39)

---

### wasInformedBy

**URI:** `http://www.w3.org/ns/prov#wasInformedBy`

**Description:** An activity a2 is dependent on or informed by another activity a1, by way of some unspecified entity that is generated by a1 and used by a2.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### wasInvalidatedBy

**URI:** `http://www.w3.org/ns/prov#wasInvalidatedBy`

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

---

### wasQuotedFrom

**URI:** `http://www.w3.org/ns/prov#wasQuotedFrom`

**Description:** An entity is derived from an original entity by copying, or 'quoting', some or all of it.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### wasRevisionOf

**URI:** `http://www.w3.org/ns/prov#wasRevisionOf`

**Description:** A revision is a derivation that revises an entity into a revised version.

**Domain:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---

### wasStartedBy

**URI:** `http://www.w3.org/ns/prov#wasStartedBy`

**Description:** Start is when an activity is deemed to have started. A start may refer to an entity, known as trigger, that initiated the activity.

**Domain:**
- [http://www.w3.org/ns/prov#Activity](http://www.w3.org/ns/prov#Activity)

**Range:**
- [http://www.w3.org/ns/prov#Entity](http://www.w3.org/ns/prov#Entity)

---


