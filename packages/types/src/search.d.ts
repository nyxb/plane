import { ICycle } from "./cycle";
import { TIssue } from "./issues/issue";
import { IModule } from "./module";
import { TPage } from "./pages";
import { IProject } from "./project";
import { IUser } from "./users";
import { IWorkspace } from "./workspace";

export type TSearchEntities =
  | "user_mention"
  | "issue_mention"
  | "project_mention"
  | "cycle_mention"
  | "module_mention"
  | "page_mention";

export type TUserSearchResponse = {
  member__avatar_url: IUser["avatar_url"];
  member__display_name: IUser["display_name"];
  member__id: IUser["id"];
};

export type TProjectSearchResponse = {
  name: IProject["name"];
  id: IProject["id"];
  identifier: IProject["identifier"];
  logo_props: IProject["logo_props"];
  workspace__slug: IWorkspace["slug"];
};

export type TIssueSearchResponse = {
  name: TIssue["name"];
  id: TIssue["id"];
  sequence_id: TIssue["sequence_id"];
  project__identifier: IProject["identifier"];
  project_id: TIssue["project_id"];
  priority: TIssue["priority"];
  state_id: TIssue["state_id"];
  type_id: TIssue["type_id"];
};

export type TCycleSearchResponse = {
  name: ICycle["name"];
  id: ICycle["id"];
  project_id: ICycle["project_id"];
  project__identifier: IProject["identifier"];
  status: ICycle["status"];
  workspace__slug: IWorkspace["slug"];
};

export type TModuleSearchResponse = {
  name: IModule["name"];
  id: IModule["id"];
  project_id: IModule["project_id"];
  project__identifier: IProject["identifier"];
  status: IModule["status"];
  workspace__slug: IWorkspace["slug"];
};

export type TPageSearchResponse = {
  name: TPage["name"];
  id: TPage["id"];
  logo_props: TPage["logo_props"];
  projects__id: TPage["project_ids"];
  workspace__slug: IWorkspace["slug"];
};

export type TSearchResponse = {
  cycle_mention?: TCycleSearchResponse[];
  issue_mention?: TIssueSearchResponse[];
  module_mention?: TModuleSearchResponse[];
  page_mention?: TPageSearchResponse[];
  project_mention?: TProjectSearchResponse[];
  user_mention?: TUserSearchResponse[];
};

export type TSearchEntityRequestPayload = {
  count: number;
  query_type: TSearchEntities[];
  query: string;
};
