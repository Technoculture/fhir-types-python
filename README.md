# FHIR-Types-Python

> Acknowledgement: Based on a fork of the amazing open source library by [Aidbox](https://aidbox.app/)
>
> ### Why Fork?
> - Integrate with db per user architecture
> - Provide a pythonic, higher level API over FHIR

## Install

```shell
pip install git+https://github.com/Technoculture/fhir-types-python
```

## Auth
TODO

## Example

```python
from elladb.resource.appointment import Appointment, Appointment_Participant
from elladb.resource.patient import Patient
from elladb.resource.practitioner import Practitioner
from elladb.base import Reference, HumanName

import requests

patient = Patient(name=[HumanName(family="Bourne", given=["Jason"])])
practitioner = Practitioner(name=[HumanName(family="Smith", given=["John"])])

patient.save()
practitioner.save()

try:
    Appointment(
        status="booked",
        participant=[
            Appointment_Participant(
                status="accepted",
                actor=Reference(reference="Practitioner/" + (practitioner.id or "")),
            ),
            Appointment_Participant(
                status="accepted",
                actor=Reference(reference="Patient/" + (patient.id or "")),
            ),
        ],
    ).save()
except requests.exceptions.RequestException as e:
    if e.response is not None:
        print(e.response.json())
```

## API

#### Save resource to elladb `.save()`

```python
from elladb.resource.patient import Patient
from elladb.base import HumanName

patient = Patient()
patient.name = [HumanName(family="Bourne", given=["Jason"])]

patient.save()
```

#### Delete resource by id `.delete()`

```python
from elladb.resource.patient import Patient

patient = Patient(id="patient-1")
patient.delete()
```

#### Get resource by id `.from_id()`

```python
from elladb.resource.patient import Patient

patient = Patient.from_id("patient-1")
```

#### Get resource list `.get()`

```python
from elladb.resource.patient import Patient
from elladb.base import Page, Count, Sort, Where

patients = Patient.get(Where('active', True), Count(10), Page(3), Sort('created_at', 'desc'))
```

#### Authorized request to any of elladb endpoints `.request()`

```python
from elladb.base import API

API.request(endpoint="/EllaTask", method="GET")

API.request(
    endpoint="/rpc",
    method="POST",
    json={
        "method": "awf.task/list",
        "params": { "filter": { "excludeDefinitions": ["awf.workflow/decision-task"] }},
    },
)
```

#### Serialize to JSON `dumps()`

```python
from elladb.resource.patient import Patient
from elladb.base import Page, Count, Sort, Where

patient = Patient.from_id('patient-1')
patient_json = patient.dumps(exclude_unset=True)
```

#### Bundle `.bundle()`

```python
from elladb.base import API

entry = []

entry.append(
    {
        "resource": patient.dumps(exclude_unset=True),
        "request": {"method": "POST", "url": "Patient"},
    },
    {
        "resource": patient.dumps(exclude_unset=True),
        "request": {"method": "POST", "url": "Patient"},
    },
)

try:
    API.bundle(entry=entry, type="transaction")
except requests.exceptions.RequestException as e:
    if e.response is not None:
        print(e.response.json())
```
