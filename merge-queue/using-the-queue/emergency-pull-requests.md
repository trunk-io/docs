# Emergency pull requests

Emergency merges bypass the queue entirely and push directly to your main branch. This is the **most disruptive action** you can take and should be reserved for true emergencies only.

{% hint style="danger" %}
**Warning:** Emergency merges bypass all safety checks. Use sparingly.
{% endhint %}

### **Emergency bypass**

If you need to completely bypass the merge queue, you can merge the PR directly through GitHub as you normally would. The merge queue will restart everything currently testing to account for the new head of the merge branch. However, this means your emergency PR won't be validated by the merge queue's predictive testing.

#### **Recommended approach**

Use [PR Prioritization](../optimizations/priority-merging.md) to fast-track your PR through the queue while still validating it:

```
/trunk merge --priority=urgent
```

The `urgent` priority is the only level that will interrupt currently testing PRs. Your PR will immediately begin testing, and other PRs will restart after yours completes.
