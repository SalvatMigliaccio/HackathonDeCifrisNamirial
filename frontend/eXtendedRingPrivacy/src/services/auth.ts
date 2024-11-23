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
        fetch(`${AUTHAPI}/api/login`, 
            {
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                method: 'POST',
                body: `username=${email}&password=${password}`,
            }).then((response) => {
                if (response.ok) {
                    response.json().then((data) => {
                        console.log({data});
                        document.cookie = `token=${data.token}`;
                        window.location.href = '/dashboard';
                    });
                } else {
                    alert('Login failed');
                }
            });}


    

    public async signIn(username:string, email: string, password_hash: string): Promise<any> {
      
      return await fetch(`${AUTHAPI}/api/users/`, { method: `POST`, headers: {"Content-Type": "application/json"}, body: JSON.stringify({ username, email, password_hash }) });
 
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

        return await fetch(`/api/users?email=${email}`, { method: 'GET' });

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