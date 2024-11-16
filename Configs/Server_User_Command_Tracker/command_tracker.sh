#!/bin/bash

LOG_MESSAGE="${$'$(whoami)@$(echo $SSH_CONNECTION | awk \'{print $1}\')'} ${'$(loginctl session-status | head -n 1 | xargs)'} [$$]: ${'$(history 1 | sed "s/^[ ]*[0-9]\+[ ]*//" )'} [${'$?'}]"

export PROMPT_COMMAND="logger -p local6.debug \"$LOG_MESSAGE\""


# Create config file at path:  /etc/rsyslog.d/config.conf
# Inside file add path for storing logs: local6.*       /var/log/user-commands.log
# sudo systemctl restart rsyslog.service
# I'm not sure how this will work on a system other than RHEL, but still it should work.