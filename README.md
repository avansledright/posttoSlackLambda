# posttoSlackLambda
This function will post a message informing you of a file upload to an S3 bucket. The message includes the file name.

You need to get an OAuth key from Slack to make this work. If you unfamiliar with Slack applications feel free to message me.

Set the enivornment variable "slackBot" to be your OAuth key.  You will also need your Channel ID. This is easily found by right clicking on the channel in the Slack desktop application and opening it in a web browswer.

Packages Required for you to bundle:
- Slack
- Slackclient
