---
description: The security and privacy of your Trunk Platform usage
---

# Security

At Trunk, we prioritize the security and privacy of your data. Here's how we protect your information when using Trunk Merge Queue and Flaky Tests.

### What data we access

#### Merge Queue

Trunk Merge Queue integrates with your GitHub repository via our GitHub App to safely automate code merging. Here's what we access:

* **GitHub repository metadata**: Repository structure, branch information, and pull request data necessary for merge operations
* **Pull request details**: PR titles, descriptions, commit information, and test results to determine merge eligibility
* **CI/CD status checks**: Results from your CI jobs to validate code before merging
* **GitHub webhook events**: Real-time notifications about PR updates and CI status changes

**What we do NOT access:**

* We do not clone or store your entire codebase
* Your source code remains in your GitHub repository

#### Flaky Tests

Flaky Tests works by uploading test results from your CI jobs to Trunk's backend for analysis. Here's what we collect:

* **Test results**: Test reports in standard formats (JUnit XML, XCResult, Bazel BEP JSON, RSpec JSON) containing:
  * Test names and identifiers
  * Pass/fail status
  * Test execution time and duration
  * Error messages and stack traces from failed tests
  * Test suite organization and hierarchy
* **CI job metadata**: Job names, build IDs, branch names, commit SHAs, and timestamps
* **Build statistics**: CI job timing data, test count, and historical performance metrics
* **Repository information**: Repository name and organization details

**How uploads work:**

* Test results are uploaded from your CI environment after tests complete
* Uploads use your organization-specific API token for authentication
* All data is transmitted over encrypted connections (TLS)
* You control which CI jobs upload results and when

**What we do NOT collect:**

* Full source code or proprietary business logic
* Sensitive environment variables or secrets
* Customer data processed by your applications
* Test execution logs beyond standard test framework outputs

**Data retention:** Test results and analytics data are retained for 45 days to provide historical flakiness analysis and trends over time.

### How we protect your data

#### Infrastructure Security

* **Hosting**: All services are hosted on Amazon Web Services (AWS) in physically secure, U.S.-based data centers with 24/7 on-site security and access monitoring
* **Encryption in transit**: All data transmitted to and from Trunk uses TLS (Transport Layer Security) and HSTS
* **Encryption at rest**: All customer data is encrypted using AES-256
* **Network isolation**: Production services run in isolated AWS VPCs with restricted access; all services are within private subnets with no internet access and use a network gateway to permit specific traffic

#### Access Controls

* **Authentication**: Multi-factor authentication (MFA) required for access to sensitive systems and applications
* **Principle of least privilege**: Access to customer data is limited to authorized personnel with business need
* **Unique user accounts**: All access requires unique user credentials; no shared accounts
* **Access monitoring**: All access to production environments is logged and monitored for security purposes
* **Access reviews**: User access is reviewed annually to ensure appropriate permissions
* **Immediate revocation**: System access is revoked within one business day of employee termination

#### Security Monitoring & Testing

* **Continuous monitoring**: Automated logging and alerting for security events; alerts are sent to appropriate personnel and corrective actions are performed as necessary
* **Vulnerability scanning**: Quarterly automated vulnerability scans to identify and remediate security issues
* **Penetration testing**: Annual third-party penetration tests using industry-standard methodologies
* **Incident response**: Formal incident response plan with defined procedures for security events

### Compliance & Auditing

#### SOC 2 Type II Certified

Trunk maintains **SOC 2 Type II compliance**, demonstrating our commitment to:

* **Security**: Protection against unauthorized access
* **Availability**: System uptime and reliability
* **Confidentiality**: Protection of sensitive information

Our most recent SOC 2 Type II audit confirmed that:

* Controls were suitably designed throughout the period
* Controls operated effectively throughout the period
* No significant security incidents occurred during the audit period

**To request a copy of our SOC 2 report**, please contact us at [security@trunk.io](mailto:security@trunk.io)
