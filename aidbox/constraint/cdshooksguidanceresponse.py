from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Cdshooksguidanceresponse(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/cdshooksguidanceresponse"])
	dataRequirement: Optional[List[DataRequirement]] = None
	moduleCanonical: Optional[str] = None
	encounter: Optional[Reference] = None
	reasonCode: Optional[List[CodeableConcept]] = None
	outputParameters: Optional[Reference] = None
	evaluationMessage: Optional[List[Reference]] = None
	requestIdentifier: Identifier
	note: Optional[List[Annotation]] = None
	status: str
	result: Optional[Reference] = None
	identifier: List[Identifier]
	moduleCodeableConcept: Optional[CodeableConcept] = None
	moduleUri: str
	occurrenceDateTime: Optional[str] = None
	subject: Optional[Reference] = None
	performer: Optional[Reference] = None
	reasonReference: Optional[List[Reference]] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None