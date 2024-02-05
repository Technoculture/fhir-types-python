from pydantic import BaseModel
from typing import Optional, List, Literal
from base import *


class Questionnaire_Item_EnableWhen(BackboneElement):
	answerQuantity: Optional[Quantity] = None
	answerDecimal: Optional[str] = None
	answerDate: Optional[str] = None
	answerReference: Optional[Reference] = None
	answerInteger: Optional[int] = None
	question: str
	answerDateTime: Optional[str] = None
	answerString: Optional[str] = None
	operator: str
	answerBoolean: Optional[bool] = None
	answerCoding: Optional[Coding] = None
	answerTime: Optional[str] = None

class Questionnaire_Item_AnswerOption(BackboneElement):
	valueInteger: Optional[int] = None
	valueDate: Optional[str] = None
	valueTime: Optional[str] = None
	valueString: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueReference: Optional[Reference] = None
	initialSelected: Optional[bool] = None

class Questionnaire_Item_Initial(BackboneElement):
	valueReference: Optional[Reference] = None
	valueUri: Optional[str] = None
	valueTime: Optional[str] = None
	valueDecimal: Optional[str] = None
	valueQuantity: Optional[Quantity] = None
	valueString: Optional[str] = None
	valueBoolean: Optional[bool] = None
	valueDateTime: Optional[str] = None
	valueDate: Optional[str] = None
	valueCoding: Optional[Coding] = None
	valueInteger: Optional[int] = None
	valueAttachment: Optional[Attachment] = None

class Questionnaire_Item(BackboneElement):
	enableBehavior: Optional[str] = None
	definition: Optional[str] = None
	linkId: str
	repeats: Optional[bool] = None
	item: Optional[List[str]] = None
	type: str
	enableWhen: Optional[List[Questionnaire_Item_EnableWhen]] = None
	answerOption: Optional[List[Questionnaire_Item_AnswerOption]] = None
	prefix: Optional[str] = None
	readOnly: Optional[bool] = None
	answerValueSet: Optional[str] = None
	code: Optional[List[Coding]] = None
	initial: Optional[List[Questionnaire_Item_Initial]] = None
	maxLength: Optional[int] = None
	required: Optional[bool] = None
	text: Optional[str] = None

class CqfQuestionnaire(BaseModel):
	meta: Meta = Meta(profile=["http://hl7.org/fhir/StructureDefinition/cqf-questionnaire"])
	description: Optional[str] = None
	subjectType: Optional[List[str]] = None
	date: Optional[str] = None
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: Optional[List[CodeableConcept]] = None
	derivedFrom: Optional[List[str]] = None
	purpose: Optional[str] = None
	name: Optional[str] = None
	item: Optional[List[Questionnaire_Item]] = None
	useContext: Optional[List[UsageContext]] = None
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	title: Optional[str] = None
	status: str
	url: Optional[str] = None
	code: Optional[List[Coding]] = None
	identifier: Optional[List[Identifier]] = None
	lastReviewDate: Optional[str] = None
	version: Optional[str] = None
	contact: Optional[List[ContactDetail]] = None
	effectivePeriod: Optional[Period] = None
	text: Optional[Narrative] = None
	contained: Optional[List[Resource]] = None
	extension: Optional[List[Extension]] = None
	modifierExtension: Optional[List[Extension]] = None
	id: Optional[str] = None
	implicitRules: Optional[str] = None
	language: Optional[str] = None