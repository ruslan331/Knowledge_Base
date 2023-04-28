from __future__ import annotations

from typing import Callable

from person import Person


ruslan = Person(name="Ruslan")
roman = Person(name="Roman")
kate = Person(name="Kate")
dmytro = Person(name="Dmytro")
volodymyr = Person(name="Volodymyr")

people = [ruslan, roman, kate, dmytro, volodymyr]
"""
Base predicates:

have experience
prepared for interview
know english
goes to parties
know technologies
studies a lot

RULES:
1. X is prepared for interview -> X knows technologies
2. X knows English AND X has experience -> X gets the job
3. X knows technologies AND X studies a lot -> X gets the job
4. X does not go to parties -> X studies a lot
5. X goes to parties -> X doesn't study a lot
5. (X doesn't know English OR doesnt have experience) AND (X doesn't know technologies OR X doesn't study a lot) -> X fails
"""

# Procedures (P)
# Use command pattern: try to find existing fact in DB;
# if can't find one, pass the responsibility down the tree
def has_experience(p: Person):
    have_experience_fact = fact_dictionary.get(has_experience).get(p)
    if have_experience_fact is True:
        return True
    elif have_experience_fact is False:
        return False
    else:
        return None

def prepared_for_interview(p: Person):
    prepared_for_interview_fact = fact_dictionary.get(prepared_for_interview).get(p)
    if prepared_for_interview_fact is True:
        return True
    elif prepared_for_interview_fact is False:
        return False
    else:
        return None

def knows_english(p: Person):
    know_english_fact = fact_dictionary.get(knows_english).get(p)
    if know_english_fact is True:
        return True
    elif know_english_fact is False:
        return False
    else:
        return None

def goes_to_parties(p: Person):
    goes_to_parties_fact = fact_dictionary.get(goes_to_parties).get(p)
    if goes_to_parties_fact is True:
        return True
    elif goes_to_parties_fact is False:
        return False
    else:
        return None

def knows_technologies(p: Person):
    know_technologies_fact = fact_dictionary.get(knows_technologies).get(p)
    if know_technologies_fact is True:
        return True
    elif know_technologies_fact is False:
        return False
    else:
        prepared_for_interview_fact = fact_dictionary.get(prepared_for_interview).get(p)
        if prepared_for_interview_fact is True:
            return True
        elif prepared_for_interview_fact is False:
            return None
        elif prepared_for_interview_fact is None:
            result = prepared_for_interview(p)
            if result:
                return True
        return None

def studies_a_lot(p: Person):
    studies_a_lot_fact = fact_dictionary.get(studies_a_lot).get(p)
    if studies_a_lot_fact is True:
        return True
    elif studies_a_lot_fact is False:
        return False
    else:
        does_party_fact = fact_dictionary.get(goes_to_parties).get(p)
        if does_party_fact is False:
            return True
        elif does_party_fact is True:
            return False
        else:
            return None


def will_pass_exam(p: Person):
    person_knows_english = knows_english(p)
    person_has_experience = has_experience(p)
    person_knows_technologies = knows_technologies(p)
    does_person_study_a_lot = studies_a_lot(p)
    if (person_knows_english is True and person_has_experience is True)\
            or (person_knows_technologies is True and does_person_study_a_lot is True):
        return True
    elif (person_knows_english is False or person_has_experience is False)\
            and (person_knows_technologies is False or does_person_study_a_lot is False):
        return False
    else:
        return None


fact_dictionary: dict[Callable, dict[Person, bool | None]] = {
    knows_english: {
        ruslan: True,
        dmytro: True,
        kate: False,
        roman: None,
        volodymyr: None
    },
    goes_to_parties: {},
    knows_technologies: {},
    studies_a_lot: {},
    prepared_for_interview: {},
    has_experience: {}
}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for person in people:
        print(f'Does {person.name} have experience?')
        x = input()
        if x == "yes":
            fact_dictionary[has_experience][person] = True
        elif x == "no":
            fact_dictionary[has_experience][person] = False
        elif x == "idk":
            fact_dictionary[has_experience][person] = None

        print(f'Does {person.name} go to parties?')
        x = input()
        if x == "yes":
            fact_dictionary[goes_to_parties][person] = True
        elif x == "no":
            fact_dictionary[goes_to_parties][person] = False
        elif x == "idk":
            fact_dictionary[goes_to_parties][person] = None

        print(f'Is {person.name} prepared for an interview?')
        x = input()
        if x == "yes":
            fact_dictionary[prepared_for_interview][person] = True
        elif x == "no":
            fact_dictionary[prepared_for_interview][person] = False
        elif x == "idk":
            fact_dictionary[prepared_for_interview][person] = None

        will_pass = will_pass_exam(person)
        if will_pass is True:
            print(f"Will {person.name} get the job: yes!")
        elif will_pass is False:
            print(f"Will {person.name} get the job: no!")
        else:
            print(f"Will {person.name} get the job: not enough information...")