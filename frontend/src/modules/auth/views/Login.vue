<template>
    <div class="row p-0 m-0">

        <div class="col-sm-12 col-lg-6 box p-0 m-0 bg-primary">
            <img src="https://images.unsplash.com/photo-1579226905180-636b76d96082?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80" alt="">
        </div>

        <div class="col-sm-12 col-lg-6 align-self-center">

            <form class="px-5" @submit.prevent="onSubmit">			

                <h2 class="text-center mb-3">Iniciar Sesion</h2>    

                <div class="form-floating mb-3">
                    <input v-model="loginForm.username" type="text" class="form-control" id="floatingInput" placeholder="Nombre de usuario">
                    <label for="floatingInput">Correo Electronico</label>
                </div>

                <div class="form-floating mb-3">
                    <input v-model="loginForm.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
                    <label for="floatingPassword">Contraseña</label>
                </div>

                <div class="text-center">
                    <button type="submit" class="btn btn-indigo mb-3">Entrar</button>
                </div>

                <p class="text-center">
                    ¿No tienes cuenta?<router-link :to="{ name: 'register' }"> !Registrate ya aqui!...</router-link>
                </p>
                
                <p class="text-center ">
                    <a href="#">¿Olvidaste tu contraseña?</a>
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

        const { loginUser } = useAuth()

        const loginForm = ref(
            {
                username: "",
                password: "",
            }
        )

        return {
            loginForm,
            onSubmit: async() => {
               const { ok, message } = await loginUser( loginForm.value )
               
               if ( !ok ) {
                   Swal.fire('Error', message, 'error')
               } 
               else  {
                   Swal.fire(
                    {
                        title:'Inicio Exitoso',
                        text:'Binevenido a LUMAYO',
                        icon:'success',
                        allowEscapeKey:false,
                        allowOutsideClick:false
                    }
                    ).then((result) => 
                        {
                            if (result.isConfirmed) {
                               router.push({ name: 'home' }) 
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