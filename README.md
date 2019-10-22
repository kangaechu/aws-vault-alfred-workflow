aws-vault-alfred-workflow
=====================

Open the AWS management console via aws-vault.

![mymovie](https://user-images.githubusercontent.com/989985/67284090-dea23e00-f50f-11e9-9ce5-a94d53e39a5f.gif)

## Overview

aws-vault is a tool for securely managing AWS credentials and authenticating multiple AWS accounts via assumeRole. `aws-vault login` is useful, but the browser cannot open multiple AWS accounts at the same time. This workflow creates a browser profile for each AWS account and opens a window for each profile.
It allows you to open multiple AWS accounts at the same time.

## How to use

`aws [profile name]`

The profile name corresponds to the profile name in `$HOME/.aws/config`.
Internally launch the `aws-vault login` command and launch Chrome with a separate profile.

## Requirements

1. [Alfred 4 or later](https://www.alfredapp.com/#download)
1. [Alfred Powerpack](https://www.alfredapp.com/shop/)
1. [aws-vault](https://github.com/99designs/aws-vault)

## Installing

1. Download workflow from [packal](http://www.packal.org/workflow/open-aws-aws-vault) or [Release](https://github.com/kangaechu/aws-vault-alfred-workflow/releases).
2. Double-click to import into Alfred.
