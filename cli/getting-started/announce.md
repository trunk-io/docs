# Announce

### Trunk Announce

Does your Git commit carry some important information to share with the rest of your organization? Now you can easily share it with the rest of the org by including `/trunk announce` at the beginning of one of the lines of your commit message.&#x20;

{% hint style="info" %}
If your org squashes commit messages, you should put it in your PR description
{% endhint %}

Any additional text on that line will form an optional title, and the remaining text of the commit message will form the commit body (both are optional, but either a title or body is required). These will then be displayed to other users when they pull or rebase.

### Enable Trunk Announce

Trunk Announce is a Git hook triggered Trunk Action. You can enable this Trunk Action by running this command:

```
trunk actions enable trunk-announce
```

### Viewing Announcements

When you pull new changes, new announcements are automatically shown.

If you would like to see changes since some commit, use  `trunk show-announcements since <ref>`.

For example:

```
 trunk show-announcements since HEAD~1
```
