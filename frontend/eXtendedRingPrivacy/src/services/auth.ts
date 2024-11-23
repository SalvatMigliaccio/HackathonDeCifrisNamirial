const AUTHAPI = 'http://localhost:8001';

class AuthService {
    private static instance: AuthService;

    private constructor() {}

    public static getInstance(): AuthService {
        if (!AuthService.instance) {
            AuthService.instance = new AuthService();
        }
        return AuthService.instance;
    }

    public async login(email: string, password: string): Promise<any> {
        return await fetch('${AUTHAPI}/api/login', { method: 'POST', body: JSON.stringify({ username:email, password }) });
    }

    public async signIn(username:string, email: string, password: string): Promise<any> {
      
      return await fetch('${AUTHAPI}/api/users/', { method: 'POST', body: JSON.stringify({ username, email, password }) });
 
    }

    public async getMe(): Promise<any> {
        const token = document.cookie.split(';')?.find((cookie) => cookie.trim().startsWith('token='))?.split('=')[1];
        return await fetch('${AUTHAPI}/api/users/me', { method: 'GET', headers: 
            {
                Authorization: `Bearer ${token}`,
            }
         });
    }


    public async getUserByEmail(email: string): Promise<any> {
        // Implement get_user_by_email logic here
        // Example:
        // return await fetch(`/api/users?email=${email}`, { method: 'GET' });
    }

    public async getMyGroups(): Promise<any> {
        const token = document.cookie.split(';')?.find((cookie) => cookie.trim().startsWith('token='))?.split('=')[1];
        return await fetch('${AUTHAPI}/api/users/me?groups', { method: 'GET', headers: 
            {
                Authorization: `Bearer ${token}`,
            }
         });
    }
}

export default AuthService.getInstance();