# jsonvalidation

## Результаты работы скрипта на данных из папки 'task_folder'

1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json
   ERROR # 1:  'unique_id' is a required property
      In schema	->	required properties of data:   ['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']
      In file	->	properties of data:   ['id', 'rr_id', 'labels', 'timestamp']

   ERROR # 2:  'user' is a required property
      In schema	->	required properties of data:   ['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']
      In file	->	properties of data:   ['id', 'rr_id', 'labels', 'timestamp']

   ERROR # 3:  'user_id' is a required property
      In schema	->	required properties of data:   ['id', 'labels', 'rr_id', 'timestamp', 'unique_id', 'user', 'user_id']
      In file	->	properties of data:   ['id', 'rr_id', 'labels', 'timestamp']


297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json
   ERROR # 1:  'type' is a required property
      In schema	->	required properties of data[type_ranges][items]:   ['date', 'type']
      In file	->	properties of data[type_ranges][29]:   ['date']

   ERROR # 2:  'type' is a required property
      In schema	->	required properties of data[type_ranges][items]:   ['date', 'type']
      In file	->	properties of data[type_ranges][31]:   ['date']

   ERROR # 3:  'type' is a required property
      In schema	->	required properties of data[type_ranges][items]:   ['date', 'type']
      In file	->	properties of data[type_ranges][33]:   ['date']


29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
   ERROR # 1:  JSON file contains nothing


2e8ffd3c-dbda-42df-9901-b7a30869511a.json
   ERROR # 1:  Unable to find or load defined Schema
      In file	->	defined Schema:   'meditation_created'


3ade063d-d1b9-453f-85b4-dda7bfda4711.json
   ERROR # 1:  Unable to find or load defined Schema
      In file	->	defined Schema:   'cmarker_calculated'


6b1984e5-4092-4279-9dce-bdaa831c7932.json
   ERROR # 1:  Unable to find or load defined Schema
      In file	->	defined Schema:   'meditation_created'


a95d845c-8d9e-4e07-8948-275167643a40.json
   ERROR # 1:  JSON file contains nothing


ba25151c-914f-4f47-909a-7a65a6339f34.json
   ERROR # 1:  Unable to find or load defined Schema
      In file	->	defined Schema:   'label_       selected'


bb998113-bc02-4cd1-9410-d9ae94f53eb0.json
   ERROR # 1:  'unique_id' is a required property
      In schema	->	required properties of data:   ['source', 'timestamp', 'finish_time', 'activity_type', 'time_start', 'unique_id']
      In file	->	properties of data:   ['info', 'points_date', 'points', 'source', 'timestamp', 'time_start', 'finish_time', 'phases_info', 'type_ranges', 'activity_type']


c72d21cf-1152-4d8e-b649-e198149d5bbb.json
   ERROR # 1:  Unable to find or load defined Schema
      In file	->	defined Schema:   'meditation_created'


cc07e442-7986-4714-8fc2-ac2256690a90.json
   ERROR # 1:  None is not of type 'object'
      In schema	->	type of data must be:   object
      In file	->	value of data:   None


e2d760c3-7e10-4464-ab22-7fda6b5e2562.json
   ERROR # 1:  'bad user id' is not of type 'integer'
      In schema	->	type of data[user_id] must be:   integer
      In file	->	value of data[user_id]:   bad user id


fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json
   ERROR # 1:  'cmarkers' is a required property
      In schema	->	required properties of data:   ['cmarkers', 'datetime', 'user_id']
      In file	->	properties of data:   ['id', 'cmarker', 'user_id', 'datetime']


ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json
   ERROR # 1:  'suprt marker' is not of type 'array'
      In schema	->	type of data[cmarkers] must be:   array
      In file	->	value of data[cmarkers]:   suprt marker

   ERROR # 2:  None is not of type 'integer'
      In schema	->	type of data[user_id] must be:   integer
      In file	->	value of data[user_id]:   None


