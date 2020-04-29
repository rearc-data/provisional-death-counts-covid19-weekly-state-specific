import os
import boto3
import urllib.request

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://data.cdc.gov/resource/pj7m-y5uh'

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(
		source_dataset_url + '.csv', '/tmp/' + new_filename + '.csv')
	urllib.request.urlretrieve(
		source_dataset_url + '.json', '/tmp/' + new_filename + '.json')

	#uploading new s3 dataset
	s3 = boto3.client('s3')

	s3.upload_file('/tmp/' + new_filename + '.json', s3_bucket, new_s3_key + '.json')
	s3.upload_file('/tmp/' + new_filename + '.csv', s3_bucket, new_s3_key + '.csv')
