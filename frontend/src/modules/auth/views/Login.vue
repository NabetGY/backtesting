<template>

    <v-row>
        <v-col cols="12" md="6" class="d-none d-md-block">
            <v-img src="https://images.unsplash.com/photo-1579226905180-636b76d96082?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80" 
                alt=""
                max-height="550"
                contain
                class="">
            </v-img>
        </v-col>

        <v-col cols="12" md="6" class="py-16">

            <h1 class="text-center mb-10">Inicio de Sesion</h1>

            <v-form ref="form" v-model="valid" lazy-validation>

                <v-text-field
                    append-icon="mdi-email"
                    v-model="loginForm.email"
                    :rules="rules.emailRules"
                    label="Correo electronico"
                    required
                ></v-text-field>

                <v-text-field
                    :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[rules.required, rules.emailMatch]"
                    :type="show4 ? 'text' : 'password'"
                    name="input-10-2"
                    label="Contraseña"
                    hint="Minimo 8 caracteres"
                    v-model="loginForm.password"
                    @click:append="show4 = !show4"
                >
                </v-text-field>

                <v-btn block color="success" class="mr-4" @click="validate">
                    Entrar
                </v-btn>

                <p class="text-center mr-4 mt-4">
                    ¿No tienes cuenta?<router-link :to="{ name: 'register' }"> !Registrate ya aqui!...</router-link>
                </p>
                
                <p class="text-center mr-4 mt-4">
                    <a href="#">¿Olvidaste tu contraseña?</a>
                </p>

            </v-form>
        </v-col>

    </v-row>

</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useAuth from "../composables/useAuth"
import Swal from 'sweetalert2'


export default{

    setup() {   
        
        const show4 = ref(false)
        const valid = ref(true)
        const form = ref(null)



        const router = useRouter()

        const { loginUser } = useAuth()

        const loginForm = ref(
            {
                email: "",
                password: "",
            }
        )

        return {
            show4,
            valid,
            form,
            loginForm,

            validate() {
                form.value.validate()
            },

            rules: {
                emailRules: [
                    v => !!v || 'Correo electronico requerido!',
                    v => /.+@.+\..+/.test(v) || 'El correo tiene que ser valido',
                ],
                required: value => !!value || 'Requerido.',
                min: v => v.length >= 8 || 'Min 8 characters',
                emailMatch: () => (`The email and password you entered don't match`),
            },
            
            onSubmit: async() => {
               const { ok, message } = await loginUser( loginForm.value )
               
               if ( !ok ) {
                   Swal.fire('Error', message, 'error')
               } 
               else  {
                   Swal.fire(
                    {
                        title:'Inicio Exitoso',
                        text:'Bienvenido a G-BACKTEST',
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

.box v-img {
   width: 100%;
    max-height: 80vh; 
    object-fit: cover;
}

</style>