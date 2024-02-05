from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Provenance_Agent(BackboneElement):
	type: Optional[CodeableConcept] = None
	role: Optional[List[CodeableConcept]] = None
	who: Reference
	onBehalfOf: Optional[Reference] = None

class Provenance_Entity(BackboneElement):
	role: str
	what: Reference
	agent: Optional[List[str]] = None

class ProvenanceRelevantHistory(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/provenance-relevant-history"])
	signature: Optional[List[Signature]] = None
	occurredDateTime: Optional[str] = None
	recorded: str
	agent: List[Provenance_Agent]
	policy: Optional[List[str]] = None
	reason: Optional[List[CodeableConcept]] = None
	activity: CodeableConcept
	target: List[Reference]
	location: Optional[Reference] = None
	entity: Optional[List[Provenance_Entity]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None