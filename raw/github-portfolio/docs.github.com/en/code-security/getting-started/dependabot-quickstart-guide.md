---
source_url: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide
title: "Dependabot quickstart guide"
crawl_depth: 1
crawled_at: 2026-05-05T08:28:20Z
word_count: 1255
---

# Dependabot quickstart guide
Find and fix vulnerable dependencies you rely on with Dependabot.
## Who can use this feature?
Dependabot alerts are available for organization-owned and user-owned repositories.
## [About Dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#about-dependabot)
This quickstart guide walks you through setting up and enabling Dependabot, viewing Dependabot alerts, and updating your repository to use a secure version of the dependency.
Dependabot consists of three different features that help you manage your dependencies:
  * Dependabot alerts: Inform you about vulnerabilities in the dependencies that you use in your repository.
  * Dependabot security updates: Automatically raise pull requests to update the dependencies you use that have known security vulnerabilities.
  * Dependabot version updates: Automatically raise pull requests to keep your dependencies up-to-date.


## [Prerequisites](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#prerequisites)
For the purpose of this guide, we're going to use a demo repository to illustrate how Dependabot finds vulnerabilities in dependencies, where you can see Dependabot alerts on GitHub, and how you can explore, fix, or dismiss these alerts.
You need to start by forking the demo repository.
  1. Navigate to [https://github.com/dependabot/demo](https://github.com/dependabot/demo?ref_product=supply-chain-security&ref_type=engagement&ref_style=text).
  2. At the top of the page, on the right, click 
  3. Select an owner (you can select your GitHub personal account) and type a repository name. For more information about forking repositories, see [Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository).
  4. Click **Create fork**.


## [Enabling Dependabot for your repository](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#enabling-dependabot-for-your-repository)
You need to follow the steps below on the repository you forked in [Prerequisites](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#prerequisites).
  1. On GitHub, navigate to the main page of the repository.
  2. Under your repository name, click **Settings**.
![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)
  3. In the "Security" section of the sidebar, click 
  4. Under "Dependabot", click **Enable** for Dependabot alerts, Dependabot security updates, and Dependabot version updates.
  5. If you clicked **Enable** for Dependabot version updates, you can edit the default `dependabot.yml` configuration file that GitHub creates for you in the `/.github` directory of your repository. To enable Dependabot version updates for your repository, you typically configure this file to suit your needs by editing the default file, and committing your changes. You can refer to the snippet provided in [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#example-dependabotyml-file) for an example.


If the dependency graph is not already enabled for the repository, GitHub will enable it automatically when you enable Dependabot.
For more information about configuring each of these Dependabot features, see [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts), [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates), and [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
## [Viewing Dependabot alerts for your repository](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#viewing-dependabot-alerts-for-your-repository)
If Dependabot alerts are enabled for a repository, you can view Dependabot alerts on the 
  1. On GitHub, navigate to the main page of the repository.
  2. Under the repository name, click the 
  3. In the "Findings" section of the sidebar, select the **Dependabot** **Vulnerabilities**.
  4. Review the open alerts on the Dependabot alerts page. By default, the page displays the **Open** tab, listing the open alerts. (You'll be able to view any closed alerts by clicking **Closed**.)
![Screenshot showing the list of Dependabot alerts for the demo repository.](https://docs.github.com/assets/cb-44694/images/help/repository/dependabot-alerts-list-demo-repo.png)
You can filter Dependabot alerts in the list, using a variety of filters or labels. For more information, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts#prioritizing-dependabot-alerts). You can also use Dependabot auto-triage rules to filter out false positive alerts or alerts you're not interested in. For more information, see [About Dependabot auto-triage rules](https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules).
  5. Click the "Command Injection in lodash" alert on the `javascript/package-lock.json` file. The details page for the alert will show the following information (note that some information may not apply to all alerts):
     * Whether Dependabot created a pull request that will fix the vulnerability. You can review the suggested security update by clicking **Review security update**.
     * Package involved
     * Affected versions
     * Patched version
     * Brief description of the vulnerability
![Screenshot of the detailed page of an alert in the demo repository, showing the main information.](https://docs.github.com/assets/cb-27531/images/help/repository/alert-details-page-demo-repo.png)
  6. Optionally, you can also explore the information on the right-side of the page. Some of the information shown in the screenshot may not apply to every alert.
     * Severity
     * CVSS metrics: We use CVSS levels to assign severity levels. For more information, see [About the GitHub Advisory database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-cvss-levels).
     * Tags
     * Weaknesses: List of CWEs related to the vulnerability, if applicable
     * CVE ID: Unique CVE identifier for the vulnerability, if applicable
     * GHSA ID: Unique identifier of the corresponding advisory on the GitHub Advisory Database. For more information, see [About the GitHub Advisory database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database#about-ghsa-ids).
     * Option to navigate to the advisory on the GitHub Advisory Database
     * Option to see all of your repositories that are affected by this vulnerability
     * Option to suggest improvements for this advisory on the GitHub Advisory Database
![Screenshot of the detailed page of an alert in the demo repository, showing the information displayed on the right-side of the page.](https://docs.github.com/assets/cb-22093/images/help/repository/more-alert-details-demo-repo.png)


For more information about viewing, prioritizing, and sorting Dependabot alerts, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts).
## [Fixing or dismissing a Dependabot alert](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#fixing-or-dismissing-a-dependabot-alert)
You can fix or dismiss Dependabot alerts on GitHub. Let's continue to use the forked repository as an example, and the "Command Injection in lodash" alert described in the previous section.
  1. Navigate to the Dependabot tab for the repository. For more information, see the [Viewing Dependabot alerts for your repository](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#viewing-dependabot-alerts-for-your-repository) section above.
  2. Click an alert.
  3. Click the "Command Injection in lodash" alert on the `javascript/package-lock.json` file.
  4. Review the alert. You can: 
     * Review the suggested security update by clicking **Review security update**. This will open the pull request generated by Dependabot with the security fix.
![Screenshot of the pull request generated by Dependabot to fix the security vulnerability highlighted by the selected alert.](https://docs.github.com/assets/cb-30876/images/help/repository/dependabot-pull-request-demo-repo.png)
       * On the pull request description, you can click **Commits** to explore the commits included in the pull request.
       * You can also click **Dependabot commands and options** to learn about the commands that you can use to interact with the pull request.
       * When you're ready to update your dependency and resolve the vulnerability, merge the pull request.
     * If you decide that you want to dismiss the alert
       * Go back to the alert details page.
       * On the top-right corner, click **Dismiss alert**.
![Screenshot of the alert details page with the Dismiss alert button, dropdown menu options, and dismissal comment box outlined in orange.](https://docs.github.com/assets/cb-63399/images/help/repository/dismiss-alert-demo-repo.png)
       * Select a reason for dismissing the alert.
       * Optionally, add a dismissal comment. The dismissal comment will be added to the alert timeline and can be used as justification during auditing and reporting.
       * Click **Dismiss alert**. The alert won't appear anymore in the **Open** tab of the alert list, and you are able to view it in the **Closed** tab.


For more information about reviewing and updating Dependabot alerts, see [Viewing and updating Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/viewing-and-updating-dependabot-alerts#reviewing-and-fixing-alerts).
## [Troubleshooting](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#troubleshooting)
You may need to do some troubleshooting if:
  * Dependabot is blocked from creating a pull request to fix an alert, or
  * The information reported by Dependabot is not what you expect.


For more information, see [Dependabot errors](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-dependabot-errors) and [Vulnerable dependency detection](https://docs.github.com/en/code-security/dependabot/troubleshooting-dependabot/troubleshooting-the-detection-of-vulnerable-dependencies), respectively.
## [Next steps](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide#next-steps)
For more information about configuring Dependabot updates, see [Configuring Dependabot security updates](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates) and [Configuring Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates).
For more information about configuring Dependabot for an organization, see [Configuring Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts#managing-dependabot-alerts-for-your-organization).
For more information about viewing pull requests opened by Dependabot, see [Managing pull requests for dependency updates](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#viewing-dependabot-pull-requests).
For more information about the security advisories that contribute to Dependabot alerts, see [Browsing security advisories in the GitHub Advisory Database](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/browsing-security-advisories-in-the-github-advisory-database).
For more information about configuring notifications about Dependabot alerts, see [Configuring notifications for Dependabot alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts).
