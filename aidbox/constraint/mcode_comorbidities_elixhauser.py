from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *

class Codingcomorbiditieselixhauser(Coding):
	display: Literal["Elixhauser Comorbidity Panel"] = "Elixhauser Comorbidity Panel"
	system: Literal["http://hl7.org/fhir/us/mcode/CodeSystem/loinc-requested-cs"] = "http://hl7.org/fhir/us/mcode/CodeSystem/loinc-requested-cs"
	code: Literal["comorbidities-elixhauser"] = "comorbidities-elixhauser"

class McodeComorbiditiesElixhauserCode(CodeableConcept):
	coding: List[Codingcomorbiditieselixhauser] = [Codingcomorbiditieselixhauser()]


class Observation_ReferenceRange(BackboneElement):
	low: Optional[Quantity] = None
	high: Optional[Quantity] = None
	type: Optional[CodeableConcept] = None
	appliesTo: Optional[List[CodeableConcept]] = None
	age: Optional[Range] = None
	text: Optional[str] = None

class Observation_Component(BackboneElement):
	referenceRange: Optional[List[str]] = None
	interpretation: Optional[List[CodeableConcept]] = None
	valueTime: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueRatio: Optional[Ratio] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueSampledData: Optional[SampledData] = None
	code: CodeableConcept
	valueCodeableConcept: Optional[CodeableConcept] = None
	valuePeriod: Optional[Period] = None
	valueRange: Optional[Range] = None
	valueInteger: Optional[int] = None
	dataAbsentReason: Optional[CodeableConcept] = None

class McodeComorbiditiesElixhauser(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-comorbidities-elixhauser"])
	category: Optional[List[CodeableConcept]] = None
	referenceRange: Optional[List[Observation_ReferenceRange]] = None
	hasMember: Optional[List[Reference]] = None
	derivedFrom: Optional[List[Reference]] = None
	interpretation: Optional[List[CodeableConcept]] = None
	encounter: Optional[Reference] = None
	method: Optional[CodeableConcept] = None
	specimen: Optional[Reference] = None
	component: Optional[List[Observation_Component]] = None
	note: Optional[List[Annotation]] = None
	effectiveDateTime: Optional[str] = None
	status: str
	code: McodeComorbiditiesElixhauserCode = McodeComorbiditiesElixhauserCode()
	identifier: Optional[List[Identifier]] = None
	effectiveTiming: Optional[str] = None
	bodySite: Optional[CodeableConcept] = None
	focus: Optional[List[Reference]] = None
	issued: Optional[str] = None
	device: Optional[Reference] = None
	effectiveInstant: Optional[str] = None
	basedOn: Optional[List[Reference]] = None
	partOf: Optional[List[Reference]] = None
	valueInteger: Optional[int] = None
	subject: Optional[Reference] = None
	performer: Optional[List[Reference]] = None
	dataAbsentReason: Optional[CodeableConcept] = None
	effectivePeriod: Optional[Period] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None