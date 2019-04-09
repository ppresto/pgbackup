def local(infine, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_fileobj
    """
    client.upload_fileobj(infile, bucket, name)
