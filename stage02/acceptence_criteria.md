GIVEN a registered patient
WHEN the practitioner checks records
THEN show the appropriate patient records

GIVEN a registered patient and available practitioner
WHEN the receptionist books
THEN store with status SCHEDULED

GIVEN an unregistered patient
WHEN the receptionist registers them
THEN patient should be added to the system
