export interface Company {
  id: number;
  name: string;
  description: string | null;
  city: string;
  address: string | null;
}

export interface Vacancy {
  id: number;
  name: string;
  description: string;
  salary: number;
  company: Company | null;
}
