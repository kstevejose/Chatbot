import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebar: SidebarsConfig = {
  apisidebar: [
    {
      type: "doc",
      id: "api/financial-information-provider-api",
    },
    {
      type: "category",
      label: "Account Discovery and Linking",
      items: [
        {
          type: "doc",
          id: "api/discovered-accounts",
          label: "APi used to discover customer FIP accounts.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "api/link-accounts",
          label: "API used to link customer FIP accounts.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "api/delink-accounts",
          label: "API used to delink customer FIP accounts.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "api/verify-otp",
          label: "API used to verify the OTP",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Data Flow",
      items: [
        {
          type: "doc",
          id: "api/request-fi",
          label: "API used to request for financial information.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "api/fetch-fi",
          label: "API used to fetch financial information.",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Consent & Consent Notifications",
      items: [
        {
          type: "doc",
          id: "api/notify-consent-status",
          label: "API used to notify consent status change.",
          className: "api-method post",
        },
        {
          type: "doc",
          id: "api/send-consent-artefact",
          label: "API used to send consent artefact.",
          className: "api-method post",
        },
      ],
    },
    {
      type: "category",
      label: "Monitoring",
      items: [
        {
          type: "doc",
          id: "api/monitoring",
          label: "API used to check the availability of the FIP application.",
          className: "api-method get",
        },
      ],
    },
  ],
};

export default sidebar.apisidebar;
