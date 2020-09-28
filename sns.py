import boto3

topicname = 'subscriptiontopic'

def sns_client():
    sns = boto3.client('sns', region='us-east-1')
    """ :type : pyboto3.sns """
    return sns

def create_topic():
    return sns_client().create_topic(
        Name=topicname
    )

def gettopics():
    return sns_client().list_topics()

def gettopicattributes():
    return sns_client().get_topic_attributes(
        TopicArn=arnofthetopic
    )

def updatetopicattributes():
    return sns_client().set_topic_attributes(
        TopicArn=arnofthetopic,
        AttributeName={
            a
        }
    )

def deletetopic():
    return sns_client().delete_topic(
        TopicArn=arnofthetopic
    )

def emailsubscription():
    return sns_client().subscribe(
        TopicArn=arnofthetopic,
        Protocol='email',
        Endpoint=email_address,

    )


def sqssubscription():
    return sns_client().subscribe(
        TopicArn=arnofthetopic,
        Protocol='sqs',
        Endpoint=queueurl,

    )













if __name__ == '__main__':
    print(create_topic)
