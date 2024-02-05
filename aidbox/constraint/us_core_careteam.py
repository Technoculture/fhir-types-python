from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class CareTeam_Participant(BackboneElement):
	role: Optional[List[CodeableConcept]] = None
	member: Optional[Reference] = None
	onBehalfOf: Optional[Reference] = None
	period: Optional[Period] = None

class UsCoreCareteam(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam"])
	category: Optional[List[CodeableConcept]] = None
	managingOrganization: Optional[List[Reference]] = None
	encounter: Optional[Reference] = None
	name: Optional[str] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	participant: List[CareTeam_Participant]
	note: Optional[List[Annotation]] = None
	status: Optional[str] = None
	identifier: Optional[List[Identifier]] = None
	telecom: Optional[List[ContactPoint]] = None
	period: Optional[Period] = None
	subject: Reference
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None