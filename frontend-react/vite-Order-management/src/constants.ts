interface AuthTokens {
  accessToken: string;
  refreshToken: string;
}

export const ACCESS_TOKEN: AuthTokens["accessToken"] = "access";
export const REFRESH_TOKEN: AuthTokens["refreshToken"] = "refresh";
