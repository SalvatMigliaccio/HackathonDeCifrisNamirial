const AUTHAPI = 'http://localhost:8001';
const CRYPTAPI = 'http://localhost:8000';


class TransactionService {
    private static instance: TransactionService;

    private constructor() {
        // Private constructor to prevent instantiation
    }

    public static getInstance(): TransactionService {
        if (!TransactionService.instance) {
            TransactionService.instance = new TransactionService();
        }
        return TransactionService.instance;
    }

    // Fetch dossiers
    public async fetchDossiers() {
        const token = document.cookie.split(';')?.find((cookie) => cookie.trim().startsWith('token='))?.split('=')[1];
        return await fetch(`${AUTHAPI}/api/users/me?dossiers`, { method: 'GET', headers: 
            {
                Authorization: `Bearer ${token}`,
            }
         });
    }

    // Fetch steps of a dossier
    public async fetchDossierSteps(dossierId: string) {

        return await fetch(`${CRYPTAPI}/dossier/${dossierId}`, { method: 'GET'});
    }

    // Sign a step
    public signStep(dossier_address: string, sign: Array<number>, document_uri:string, group:number) {
        const entity_seed = ''

        return fetch(`${CRYPTAPI}/sign`, { method: 'POST', body: JSON.stringify({ sign, entity_seed, dossier_address, document_uri, group }) });
        

    }

    // Start a dossier
    public async startDossier() {
        // fetcho trans no args, recupero l'id, poi trovo l'id dell'utente corente e fetcho authai per creare dossier

        const dossier_id =(await (await fetch(`${CRYPTAPI}/dossier`, { method: 'POST' })).json())?.address;

        const token = document.cookie.split(';')?.find((cookie) => cookie.trim().startsWith('token='))?.split('=')[1];
        return await fetch(`${AUTHAPI}/dossier/link_dossier`, { method: 'POST', headers:
            {
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ dossier_address:dossier_id            })

         });

        
    }
}

export default TransactionService.getInstance();