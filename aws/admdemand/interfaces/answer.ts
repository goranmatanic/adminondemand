export interface Answer {
    name: string,
    company_size: "1-5" | "6 - 50" | "51 - 250" | ">250",
    accounting_size: "0" | "1-5" | "6 - 50" | "51 - 250" | ">250",
    creative_size: "0" | "1-5" | "6 - 50" | "51 - 250" | ">250",
    it_size: "0" | "1-5" | "6 - 50" | "51 - 250" | ">250",
}