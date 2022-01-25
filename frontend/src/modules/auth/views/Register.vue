<template>

    <div class="row p-0 m-0">

        <div class="col-sm-12 col-lg-6 box p-0 m-0 bg-primary">
            <img src="https://images.unsplash.com/photo-1579226905180-636b76d96082?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80" alt="">
        </div>
        
        <div class="col-sm-12 col-lg-6 align-self-center">
            
            <form class="px-5" @submit.prevent="onSubmit">			

                <h2 class="text-center m-1 mb-4 mt-4">Registro de usuario</h2>    

                <div class="form-floating mb-3">
                    <input v-model="registerForm.username" type="text" class="form-control" id="floatingInput" placeholder="Nombre de usuario">
                    <label for="floatingInput">Nombre de usuario</label>
                </div>

                <div class="form-floating mb-3">
                    <input v-model="registerForm.email" type="text" class="form-control" id="floatingInput" placeholder="Nombre de usuario">
                    <label for="floatingInput">Correo Electronico</label>
                </div>

                <div class="form-floating mb-3">
                    <input v-model="registerForm.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Contraseña</label>
                </div>

                <div class="text-center">
                    <button type="submit" class="btn btn-indigo mb-3">Registrate</button>
                </div>

                <p class="text-center">
                    ¿Tienes cuenta?<router-link :to="{ name: 'login' }"> !Ingresa ya aqui!...</router-link>
                </p>

            </form>
        </div>
    </div>
                
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useAuth from "../composables/useAuth"
import Swal from 'sweetalert2'


export default{

    setup() {    

        const router = useRouter()

        let file = ref(null)

        const { createUser } = useAuth()

        const registerForm = ref(
            {
                email: "",
                username: "",
                number_phone: null,
                password: "",
                image_perfil: ""
            }
        )

        return {
            file,
            registerForm,
            onFileChange: (e) => {
            let files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            file = files[0]
        },
            onSubmit: async() => {

               const { ok, message } = await createUser( registerForm.value )
               
               if ( !ok ) {
                   Swal.fire('Error', message, 'error')
               } 
               else  {
                   Swal.fire(
                    {
                        title:'Registro Exitoso',
                        text:'Ahora inicia sesion',
                        icon:'success',
                        allowEscapeKey:false,
                        allowOutsideClick:false
                    }
                    ).then((result) => 
                        {
                            if (result.isConfirmed) {
                               router.push('login') 
                            } 
                        }
                    )
                }
            },
        }
    }

}
</script>

<style scoped>

.box img {
   width: 100%;
    max-height: 100vh; 
    object-fit: cover;
}

</style>