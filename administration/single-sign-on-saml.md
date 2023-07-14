# Single Sign-On (SAML)

> 📘 Enterprise Tier Required
>
> Contact sales@trunk.io for more information

### Overview

Configuring SAML (Security Assertion Markup Language) for your Trunk account lets you and all your team log in to Trunk using the credentials stored in your organization’s identity store that has been configured with a SAML Identity Provider.

#### Prerequisites

* Trunk Enterpise Account with SAML enabled on the account. If SAML is not enabled for your organization in Trunk please reach out to support@trunk.io to enable it.
* An Identitiy Provider (IdP) that support SAML 2.0 protocols.

#### Configuring SAML

Configuring SSO in trunk is not currently self service. Please reach out to your support contact for help onboarding your organization onto our SSO solution.

#### Just in time (JIT) user provisioning

With JIT provisioning, a user is created within Trunk the first time they try to log in. This eliminates the need for administrators to manually create user accounts one at a time.

Some organizations might not want to invite all of their users to Trunk. If you would like to make changes to how SAML works for your account, contact Trunk support. It is up to the organization to configure their IdP to not send assertions to Trunk if they don’t want a particular user to access Trunk.

#### SAML strict

If you would like to enforce SAML Strict mode so other login methods are denied please reach out to your enterprise support contact at Trunk.
