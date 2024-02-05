from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class Coding108290001(Coding):
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["108290001"] = "108290001"

class CodexrtRadiotherapyTreatedPlanCategory(CodeableConcept):
	coding: List[Coding108290001] = [Coding108290001()]

class Coding1255724003(Coding):
	display: Literal["Radiotherapy treatment plan (regime/therapy)"] = "Radiotherapy treatment plan (regime/therapy)"
	system: Literal["http://snomed.info/sct"] = "http://snomed.info/sct"
	code: Literal["1255724003"] = "1255724003"

class CodexrtRadiotherapyTreatedPlanCode(CodeableConcept):
	coding: List[Coding1255724003] = [Coding1255724003()]


class Procedure_FocalDevice(BackboneElement):
	action: Optional[CodeableConcept] = None
	manipulated: Reference

class Procedure_Performer(BackboneElement):
	function: Optional[CodeableConcept] = None
	actor: Reference
	onBehalfOf: Optional[Reference] = None

class CodexrtRadiotherapyTreatedPlan(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/codex-radiation-therapy/StructureDefinition/codexrt-radiotherapy-treated-plan"])
	category: Optional[CodexrtRadiotherapyTreatedPlanCategory] = None
	report: Optional[List[Reference]] = None
	usedCode: Optional[List[CodeableConcept]] = None
	usedReference: Optional[List[Reference]] = None
	instantiatesCanonical: Optional[List[str]] = None
	instantiatesUri: Optional[List[str]] = None
	focalDevice: Optional[List[Procedure_FocalDevice]] = None
	encounter: Optional[Reference] = None
	complicationDetail: Optional[List[Reference]] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	statusReason: Optional[CodeableConcept] = None
	outcome: Optional[CodeableConcept] = None
	asserter: Optional[Reference] = None
	note: Optional[List[Annotation]] = None
	complication: Optional[List[CodeableConcept]] = None
	status: str
	recorder: Optional[Reference] = None
	code: CodexrtRadiotherapyTreatedPlanCode = CodexrtRadiotherapyTreatedPlanCode()
	identifier: Optional[List[Identifier]] = None
	bodySite: Optional[List[CodeableConcept]] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	performedPeriod: Optional[Period] = None
	location: Optional[Reference] = None
	followUp: Optional[List[CodeableConcept]] = None
	subject: Reference
	performer: Optional[List[Procedure_Performer]] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None