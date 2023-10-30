# Ecosystem: TypeScript and cds-typer in CAP

In this session Daniel will talk about TypeScript in the SAP Cloud Application Programming Model (CAP).

## Abstract

The _SAP Cloud Application Programming Model_ (CAP) is a framework for building applications with focus on accelerated, domain-centric development. While CAP is opinionated, it also prides itself in not sacrificing on the user's flexibility. When running your CAP project on the Node.js runtime, you are therefore free to enrich your project with _TypeScript_'s static type system. TypeScript is a superset of JavaScript and helps you to reason about your code without even running it. CAP caters to TypeScript users by offering types for all of its APIs.
The final gap in these type definitions has been the type information for the project's _domain model_, which is written by the user. We are now closing this gap by providing the open source tool _cds-typer_, which allows the user to convert their model written in CAP's definition language _CDS_ into TypeScript definitions. These definitions can be seamlessly integrated to get convenient code-completion from one's IDE into the lean service definitions one would typically write , empowering users to write code with even more confidence.
In this session, Daniel will give you an overview over the capabilities of CAP's type definitions and demonstrate _cds-typer_.

## Speaker

Daniel O'Grady is part of the CAP tools team and maintainer of _cds-typer_. He is a code aficionado with a fondness for type systems and considers developer experience to be just as important as user experience. Daniel believes that neither learning the signatures for API functions, nor memorising every detail of your domain model by heart should be the main focus for a programmer during speedy development cycles. Those are things best left to the computer (in this case: the type system).

## How to get involved

If you discover any bugs or gaps in _cds-typer_, you can head over to the [repository on GitHub](https://github.com/cap-js/cds-typer) and open an issue. Or even better: contribute a pull request, as the project is fully open source!

## Learning Recommendation

- [The offical TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) for getting in touch with TypeScript in general
- [CAPire section on cds-typer](https://cap.cloud.sap/docs/tools/cds-typer) to learn how to use cds-typer for your own CAP projects
- [Blog post on TypeScript in the SAP ecosystem by Mike Doyle](https://blogs.sap.com/2023/07/05/typescript-sheriff-how-can-i-use-typescript-in-the-sap-ecosystem/)
- [Initial demo of cds-typer on reCAP2023](https://broadcast.sap.com/replay/23707_reCAP2023) (starts at 1:57:10)

## Session Metadata

```yaml
- Date of Evaluation: 2024-02-06
- Development Phase:  Code
- Adoption Readiness:  Ready for Adoption
- Scopes: CAP node.js
- Topic Clusters: Developer Experience
- External Speaker: No
```

## Overview Page of Past Sessions, Onboarding Material and Newsletters

- [The overview of the past sessions, slides, recordings and more can be found on the past session page][Recordings].  The slides are attached to the MediaShare recording.
- [Collaborative Onboarding Page for new hires, colleagues switching technology stacks / roles or colleagues looking for inspiration](https://pages.github.tools.sap/Onboarding/Onboarding/#/).
- [Past Newsletters can be found in the corresponding folders](https://github.tools.sap/CloudNativeCulture/Ecosystem/tree/master/Newsletter).
 
## Registration List and Communication Channels

- If you want to **[get invitations and newsletters for all topics independent of
  the technology, you can subscribe to the Distribution List][DL]**. (VPN required)
- If you want to **[get invitations and newsletters only for JavaScript / SAPUI5
  topics, you can to the Distribution List][Event]**.
- **[Engineering Ecosystem Slack Channel #sap-engineering-ecosystem][Slack]**

[DL]: https://profiles.wdf.sap.corp/groups/5b7147227bcf84e8be00000f/users
[Event]: https://fiorilaunchpad-sapitcloud.dispatcher.hana.ondemand.com/sap/hana/uis/clients/ushell-app/shells/fiori/FioriLaunchpad.html#my-events&/ig=4328714
[Recordings]: https://github.tools.sap/CloudNativeCulture/Ecosystem/blob/master/Sessions/PastSessions.md
[Slack]: https://my.slack.com/archives/CSP54NFPZ

## Facilitator / Curator: Klaus Haeuptle

- [**If you are interested in Software Engineering and Software Architecture, you can subscribe to my external newsletter**](https://ecosystem4engineering.substack.com/p/collaboration-on-improving): Views are my own.
- The views expressed on the external channels are my own: [Substack](https://ecosystem4engineering.substack.com/), [LinkedIn](https://www.linkedin.com/in/klaus-h%C3%A4uptle-951a0349/), [Mastodon](https://saptodon.org/@klaushaeuptle#), [Twitter: @KHaeuptle](https://twitter.com/KHaeuptle) 
- Profiles: [Amazon Book Author Profile](https://www.amazon.de/~/e/B0C4NYSGD7), [Culture Ambassador Network Profile](https://jam4.sapjam.com/discussions/VwPmzklBNtL6YJgQcx0Bnj) 

[Slack]: https://my.slack.com/archives/CSP54NFPZ
