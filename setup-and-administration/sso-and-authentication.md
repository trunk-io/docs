---
description: Configure Single Sign-On (SSO) for your Trunk organization
---

# SSO and Authentication

Trunk supports Single Sign-On (SSO) for enterprise organizations that need centralized authentication and access control. This guide covers how to set up your Trunk organization with SSO, manage user access, and handle common enterprise authentication scenarios.

{% hint style="info" %}
SSO is available on the [Enterprise plan](billing.md). To enable SSO for your organization, contact [sales@trunk.io](mailto:sales@trunk.io).
{% endhint %}

## Authentication Methods

Trunk supports multiple ways to create an account and sign in:

| Method | Description | Best for |
| --- | --- | --- |
| **OAuth (Google)** | Sign in with your Google account | Teams using Google Workspace |
| **OAuth (GitHub)** | Sign in with your GitHub account | Teams using GitHub |
| **OAuth (Microsoft)** | Sign in with your Microsoft account | Teams using Microsoft Entra ID |
| **SSO (SAML)** | Sign in through your organization's identity provider | Enterprise teams with centralized identity management |

## Setting Up Trunk with SSO

### Step 1: Contact Trunk to enable SSO

SSO must be enabled by the Trunk team for your organization. To get started:

1. Email [sales@trunk.io](mailto:sales@trunk.io) with your organization name, preferred identity provider (IdP), and the email domain(s) you want to associate with SSO.
2. The Trunk team will work with you to configure SSO for your organization and provide any required configuration details (such as the SSO callback URL and entity ID) for your identity provider.

### Step 2: Configure your identity provider

Once Trunk has enabled SSO for your organization, configure your identity provider (IdP) with the settings provided by the Trunk team. Trunk supports SAML-based SSO with common identity providers including:

* **Okta**
* **Microsoft Entra ID (Azure AD)**
* **Google Workspace**
* **OneLogin**
* **Other SAML 2.0 compliant providers**

Your IdP administrator will need to:

1. Create a new SAML application for Trunk in your IdP.
2. Configure the SAML callback URL and entity ID provided by the Trunk team.
3. Set up attribute mappings (email, name) as specified by the Trunk team.
4. Assign users or groups who should have access to Trunk.

### Step 3: Create the Trunk organization

After SSO is configured, the organization administrator should:

1. Go to [app.trunk.io/signup](https://app.trunk.io/signup) and sign in using your SSO-linked email address.
2. [Create your organization](connecting-to-trunk.md#create-an-organization) with a workspace name and URL slug.
3. Verify that SSO login works correctly for your account.

{% hint style="warning" %}
**Important for organizations with restricted OAuth providers**

If your organization has disabled Google sign-in, GitHub sign-in, or other OAuth methods, make sure you sign in through the SSO option rather than OAuth. Signing in with an OAuth provider that is not associated with your corporate email may result in your Trunk account being linked to a personal email address rather than your work email.

For example, if your company uses Google Workspace but has disabled "Sign in with Google" at the organizational level, do not use a personal Gmail account to create the Trunk organization. Instead, use SSO with your corporate email or contact [support@trunk.io](mailto:support@trunk.io) to ensure your account is set up correctly.
{% endhint %}

### Step 4: Set up team access

Once the organization is created, configure how your colleagues will access Trunk. You have several options:

#### Option A: Team domains (recommended for large teams)

Configure [Team Domains](managing-your-organization.md#team-domains) to automatically grant access to anyone who signs in with an email under your company's domain. This is the simplest approach for large organizations.

1. Navigate to **Settings > Organization > Team > Domains**.
2. Click **Add Domain** and enter your company's email domain (e.g., `yourcompany.com`).
3. Any team member who creates a Trunk account with an email matching that domain will automatically be added to your organization.

#### Option B: Manual invitations

For more granular control, [invite specific team members](managing-your-organization.md#inviting-team-members) by email:

1. Navigate to **Settings > Organization > Team > Members**.
2. Click **Invite Users**.
3. Enter comma-separated email addresses and select a role (**Member** or **Admin**).

#### Option C: Combined approach

Use team domains for broad access and manually invite specific users who may have email addresses outside your primary domain.

## Managing Access with SSO

### User roles

Trunk organizations support two roles:

* **Member**: Full access to Trunk features with limited administrative permissions (default).
* **Admin**: Full administrative access, including the ability to manage team members, billing, and organization settings.

For details on managing roles, see [Managing Team Members](managing-your-organization.md#managing-team-members).

### Onboarding new team members

When a new colleague needs access to Trunk:

1. **With team domains enabled**: They simply sign in at [app.trunk.io](https://app.trunk.io) using SSO with their corporate email. They will be automatically added to your organization.
2. **Without team domains**: An admin must [send an invitation](managing-your-organization.md#inviting-team-members) to the new member's email address. The new member then signs in at [app.trunk.io](https://app.trunk.io) using SSO and accepts the invitation.

### Removing team members

Organization admins can remove team members by navigating to **Settings > Organization > Team > Members**, clicking on the member's name, and selecting **Remove**. See [Managing Team Members](managing-your-organization.md#managing-team-members) for more details.

### Monitoring pending invitations

Track outstanding invitations under **Settings > Organization > Team > Pending Invites**. From this page, you can copy invite links or revoke pending invitations. See [Pending Invites](managing-your-organization.md#pending-invites) for details.

## Troubleshooting

### My account is linked to the wrong email

If you accidentally created your Trunk account with a personal email instead of your corporate email (for example, by signing in with GitHub OAuth instead of SSO), contact [support@trunk.io](mailto:support@trunk.io) to update your account email.

### My team cannot sign in with SSO

Verify the following:

* SSO has been enabled for your organization by the Trunk team.
* Your identity provider is correctly configured with the SAML settings provided by Trunk.
* The user's email domain matches the domain configured for SSO.
* The user has been assigned to the Trunk application in your identity provider.

If issues persist, contact [support@trunk.io](mailto:support@trunk.io).

### Users are being added to the wrong organization

If team domain auto-join is placing users in an unexpected organization, verify that only one Trunk organization is configured with your company's email domain. Contact [support@trunk.io](mailto:support@trunk.io) if you need help resolving domain conflicts.

### OAuth provider is disabled by my company

If your company has disabled specific OAuth providers (for example, Google sign-in is blocked), use the SSO login option directly. Do not attempt to use a personal account with a different OAuth provider, as this will create an account that is not linked to your corporate identity.

## Frequently Asked Questions

**Is SSO required to use Trunk?**\
No. SSO is optional and available on the Enterprise plan. Teams can use OAuth (Google, GitHub, or Microsoft) to sign in without SSO.

**Can I use both SSO and OAuth?**\
Yes. Your organization can have members who sign in with SSO and others who sign in with OAuth. However, for consistent identity management, we recommend that enterprise organizations use SSO as their primary authentication method.

**What happens if SSO goes down?**\
If your identity provider experiences an outage, users who previously signed in via OAuth will still be able to access Trunk using their OAuth credentials. Contact [support@trunk.io](mailto:support@trunk.io) if you need emergency access.

**Can I enforce SSO-only login for my organization?**\
To discuss enforcing SSO-only login for your organization, contact [sales@trunk.io](mailto:sales@trunk.io).

**How do I migrate an existing Trunk organization to SSO?**\
Contact [sales@trunk.io](mailto:sales@trunk.io) to enable SSO for an existing organization. The Trunk team will help you transition your team's authentication without disrupting access.
