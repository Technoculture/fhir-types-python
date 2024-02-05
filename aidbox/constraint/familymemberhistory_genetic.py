from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class FamilyMemberHistory_Condition(BackboneElement):
	onsetRange: Optional[Range] = None
	onsetAge: Optional[str] = None
	contributedToDeath: Optional[bool] = None
	onsetPeriod: Optional[Period] = None
	outcome: Optional[CodeableConcept] = None
	note: Optional[List[Annotation]] = None
	onsetString: Optional[str] = None
	code: CodeableConcept

class FamilymemberhistoryGenetic(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/familymemberhistory-genetic"])
	deceasedAge: Optional[str] = None
	patient: Reference
	date: Optional[str] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	sex: Optional[CodeableConcept] = None
	ageRange: Optional[Range] = None
	bornString: Optional[str] = None
	deceasedBoolean: Optional[bool] = None
	name: Optional[str] = None
	relationship: CodeableConcept
	reasonCode: Optional[List[CodeableConcept]] = None
	note: Optional[List[Annotation]] = None
	status: str
	condition: Optional[List[FamilyMemberHistory_Condition]] = None
	identifier: Optional[List[Identifier]] = None
	ageString: Optional[str] = None
	deceasedRange: Optional[Range] = None
	deceasedDate: Optional[str] = None
	bornPeriod: Optional[Period] = None
	deceasedString: Optional[str] = None
	ageAge: Optional[str] = None
	bornDate: Optional[str] = None
	dataAbsentReason: Optional[CodeableConcept] = None
	reasonReference: Optional[List[Reference]] = None
	estimatedAge: Optional[bool] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None