Before running this locally, please supply 'candidate_id' in 'config.ini' with a valid guid.

# Some decisions I made while writing this
1. I choose to write each api in separate classes w/o inheritance to a shared base class. I feel this way will allow for easier maintenance in the future if someone wanted to change the arguments ingested by an api call. This does mean that delete() is the same in three files right now since those api calls are currently very similar.
2. I decided to treat the candidate_id as a secret. In a real-life sceanrio, in which the code would be deployed, I would have added the secret back in during the build process and would have made it an environment variable.
3. I choose to use print vs logging for simplicity. It seems like overkill to use logging in this situation.
