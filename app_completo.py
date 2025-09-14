import streamlit as st
import hashlib
import datetime
import uuid
import re
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() 

st.set_page_config(
    page_title="Sistema de Vacaciones Completo",
    page_icon="data:image/png;base64,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",
    layout="wide"
)
# Intentar importar Supabase
try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False
    st.error("Por favor instala Supabase: pip install supabase")

# ===================================================================
# CONFIGURACIÓN DE SUPABASE
# ===================================================================

def obtener_cliente_supabase():
    """Obtiene cliente de Supabase configurado"""
    if not SUPABASE_AVAILABLE:
        return None
    
    try:
        # Intentar obtener de streamlit secrets (producción)
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_ANON_KEY"]
        except:
            # Fallback a variables de entorno (local)
            url = os.getenv("SUPABASE_URL")
            key = os.getenv("SUPABASE_ANON_KEY")
        
        if not url or not key:
            st.error("Credenciales de Supabase no configuradas")
            return None
            
        return create_client(url, key)
    except Exception as e:
        st.error(f"Error conectando a Supabase: {e}")
        return None
# ===================================================================
# SISTEMA DE AUTENTICACIÓN CON SUPABASE
# ===================================================================

class SistemaAutenticacionSupabase:
    def __init__(self):
        self.supabase = obtener_cliente_supabase()
        if not self.supabase:
            st.error("No se pudo conectar a Supabase")
    
    def hash_password(self, password):
        """Encripta contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def crear_usuarios_default(self):
        """Crea usuarios por defecto en Supabase"""
        if not self.supabase:
            return
        
        usuarios_default = [
            {
                "username": "admin",
                "password_hash": self.hash_password("admin123"),
                "rol": "administrador",
                "nombre_completo": "Administrador del Sistema",
                "email": "admin@empresa.com",
                "empleado_asociado": None,
                "departamento": "Administración",
                "activo": True,
                "debe_cambiar_password": False,
                "intentos_fallidos": 0
            },
            {
                "username": "rrhh",
                "password_hash": self.hash_password("rrhh123"),
                "rol": "recursos_humanos",
                "nombre_completo": "Recursos Humanos",
                "email": "rrhh@empresa.com",
                "empleado_asociado": None,
                "departamento": "RRHH",
                "activo": True,
                "debe_cambiar_password": False,
                "intentos_fallidos": 0
            },
            {
                "username": "juan.perez",
                "password_hash": self.hash_password("123456"),
                "rol": "empleado",
                "nombre_completo": "Juan Pérez",
                "email": "juan.perez@empresa.com",
                "empleado_asociado": "Juan Pérez",
                "departamento": "Desarrollo",
                "activo": True,
                "debe_cambiar_password": False,
                "intentos_fallidos": 0
            },
            {
                "username": "maria.garcia",
                "password_hash": self.hash_password("123456"),
                "rol": "empleado",
                "nombre_completo": "María García",
                "email": "maria.garcia@empresa.com",
                "empleado_asociado": "María García",
                "departamento": "Marketing",
                "activo": True,
                "debe_cambiar_password": False,
                "intentos_fallidos": 0
            }
        ]
        
        for usuario in usuarios_default:
            try:
                # Verificar si ya existe
                existing = self.supabase.table('usuarios').select('id').eq('username', usuario['username']).execute()
                if not existing.data:
                    # Crear solo si no existe
                    self.supabase.table('usuarios').insert(usuario).execute()
            except Exception:
                # Usuario ya existe o error, continuar
                continue
    
    def autenticar_mejorado(self, username, password):
        """Autenticación con control de intentos fallidos"""
        if not self.supabase:
            return None, "Error de conexión a base de datos"
        
        try:
            # Buscar usuario
            result = self.supabase.table('usuarios')\
                .select('*')\
                .eq('username', username)\
                .eq('activo', True)\
                .execute()
            
            if not result.data:
                return None, "Usuario no encontrado"
            
            usuario = result.data[0]
            
            # Verificar intentos fallidos
            if usuario.get('intentos_fallidos', 0) >= 3:
                return None, "Usuario bloqueado por múltiples intentos fallidos"
            
            # Verificar contraseña
            if usuario['password_hash'] == self.hash_password(password):
                # Reset intentos fallidos
                self.supabase.table('usuarios')\
                    .update({'intentos_fallidos': 0, 'ultimo_acceso': datetime.datetime.now().isoformat()})\
                    .eq('id', usuario['id'])\
                    .execute()
                
                return usuario, "Login exitoso"
            else:
                # Incrementar intentos fallidos
                nuevos_intentos = usuario.get('intentos_fallidos', 0) + 1
                self.supabase.table('usuarios')\
                    .update({'intentos_fallidos': nuevos_intentos})\
                    .eq('id', usuario['id'])\
                    .execute()
                
                intentos_restantes = 3 - nuevos_intentos
                if intentos_restantes > 0:
                    return None, f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos."
                else:
                    return None, "Usuario bloqueado por múltiples intentos fallidos."
        
        except Exception as e:
            return None, f"Error de autenticación: {e}"
    
    def validar_email(self, email):
        """Valida formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def verificar_duplicados(self, nombre_completo, email):
        """Verifica duplicados en Supabase"""
        if not self.supabase:
            return False, "Error de conexión"
        
        try:
            # Verificar nombre
            result_nombre = self.supabase.table('usuarios')\
                .select('id')\
                .ilike('nombre_completo', nombre_completo)\
                .execute()
            
            if result_nombre.data:
                return False, f"Ya existe un usuario con el nombre '{nombre_completo}'"
            
            # Verificar email
            result_email = self.supabase.table('usuarios')\
                .select('id')\
                .ilike('email', email)\
                .execute()
            
            if result_email.data:
                return False, f"Ya existe un usuario con el email '{email}'"
            
            return True, "Sin duplicados"
        
        except Exception as e:
            return False, f"Error verificando duplicados: {e}"
    
    def generar_username_simple(self, nombre_completo):
        """Genera username simple sin verificar duplicados"""
        base = nombre_completo.lower().replace(" ", ".").replace("ñ", "n")
        base = re.sub(r'[^a-z0-9.]', '', base)
        return base
    
    def generar_username_sugerido(self, nombre_completo):
        """Genera username único verificando duplicados"""
        base = self.generar_username_simple(nombre_completo)
        
        if not self.supabase:
            return base
        
        username = base
        contador = 1
        
        while True:
            try:
                result = self.supabase.table('usuarios').select('id').eq('username', username).execute()
                if not result.data:
                    return username
                username = f"{base}{contador}"
                contador += 1
            except:
                return base
    
    def crear_solicitud_registro(self, nombre_completo, email, departamento, comentarios=""):
        """Crea solicitud de registro en Supabase"""
        if not self.supabase:
            return False, "Error de conexión"
        
        # Validaciones
        if not nombre_completo or len(nombre_completo.strip()) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"
        
        if not self.validar_email(email):
            return False, "Email inválido"
        
        valido, mensaje = self.verificar_duplicados(nombre_completo, email)
        if not valido:
            return False, mensaje
        
        try:
            # Verificar solicitud pendiente existente
            existing = self.supabase.table('solicitudes_registro')\
                .select('id')\
                .eq('email', email.lower())\
                .eq('estado', 'pendiente')\
                .execute()
            
            if existing.data:
                return False, "Ya tienes una solicitud pendiente"
            
            # Crear nueva solicitud
            nueva_solicitud = {
                "nombre_completo": nombre_completo.strip(),
                "email": email.lower().strip(),
                "departamento": departamento.strip(),
                "comentarios": comentarios.strip(),
                "estado": "pendiente"
            }
            
            self.supabase.table('solicitudes_registro').insert(nueva_solicitud).execute()
            
            # Generar username sugerido simple
            username_sugerido = self.generar_username_simple(nombre_completo)
            
            return True, f"Solicitud enviada exitosamente. Te contactaremos a {email}. Tu nombre de usuario sugerido será: {username_sugerido}"
        
        except Exception as e:
            return False, f"Error creando solicitud: {e}"
    
    def obtener_solicitudes_registro(self):
        """Obtiene solicitudes de registro"""
        if not self.supabase:
            return []
        
        try:
            result = self.supabase.table('solicitudes_registro')\
                .select('*')\
                .order('fecha_solicitud', desc=True)\
                .execute()
            return result.data
        except:
            return []
    
    def procesar_solicitud_registro(self, id_solicitud, accion, admin_user, password_temporal=None):
        """Procesa solicitud de registro"""
        if not self.supabase:
            return False, "Error de conexión"
        
        try:
            # Obtener solicitud
            solicitud_result = self.supabase.table('solicitudes_registro')\
                .select('*')\
                .eq('id', id_solicitud)\
                .eq('estado', 'pendiente')\
                .execute()
            
            if not solicitud_result.data:
                return False, "Solicitud no encontrada"
            
            solicitud = solicitud_result.data[0]
            
            if accion == "aprobar":
                # Generar username y password
                username = self.generar_username_sugerido(solicitud["nombre_completo"])
                if not password_temporal:
                    password_temporal = f"temp{datetime.datetime.now().strftime('%m%d')}"
                
                # Crear usuario
                nuevo_usuario = {
                    "username": username,
                    "password_hash": self.hash_password(password_temporal),
                    "rol": "empleado",
                    "nombre_completo": solicitud["nombre_completo"],
                    "email": solicitud["email"],
                    "empleado_asociado": solicitud["nombre_completo"],
                    "departamento": solicitud["departamento"],
                    "activo": True,
                    "debe_cambiar_password": True,
                    "intentos_fallidos": 0
                }
                
                self.supabase.table('usuarios').insert(nuevo_usuario).execute()
                
                # Crear empleado correspondiente
                empleado_data = {
                    "nombre_completo": solicitud["nombre_completo"],
                    "total_dias": 22,
                    "dias_usados": 0,
                    "departamento": solicitud["departamento"],
                    "activo": True
                }
                
                self.supabase.table('empleados').insert(empleado_data).execute()
                
                # Actualizar solicitud
                self.supabase.table('solicitudes_registro')\
                    .update({
                        "estado": "aprobada",
                        "revisada_por": admin_user["nombre_completo"],
                        "fecha_revision": datetime.datetime.now().isoformat(),
                        "username_asignado": username,
                        "password_temporal": password_temporal
                    })\
                    .eq('id', id_solicitud)\
                    .execute()
                
                mensaje = f"Usuario creado: {username} / Password: {password_temporal}"
            
            elif accion == "rechazar":
                self.supabase.table('solicitudes_registro')\
                    .update({
                        "estado": "rechazada",
                        "revisada_por": admin_user["nombre_completo"],
                        "fecha_revision": datetime.datetime.now().isoformat()
                    })\
                    .eq('id', id_solicitud)\
                    .execute()
                
                mensaje = "Solicitud rechazada"
            
            return True, mensaje
        
        except Exception as e:
            return False, f"Error procesando solicitud: {e}"
    
    def obtener_permisos(self, rol):
        """Define permisos por rol"""
        permisos = {
            "administrador": {
                "ver_dashboard": True,
                "crear_solicitudes": True,
                "ver_todas_solicitudes": True,
                "aprobar_solicitudes": True,
                "gestionar_usuarios": True,
                "gestionar_empleados": True
            },
            "recursos_humanos": {
                "ver_dashboard": True,
                "crear_solicitudes": False,
                "ver_todas_solicitudes": True,
                "aprobar_solicitudes": True,
                "gestionar_usuarios": True,
                "gestionar_empleados": True
            },
            "empleado": {
                "ver_dashboard": True,
                "crear_solicitudes": True,
                "ver_todas_solicitudes": False,
                "aprobar_solicitudes": False,
                "gestionar_usuarios": False,
                "gestionar_empleados": False
            }
        }
        return permisos.get(rol, permisos["empleado"])

# ===================================================================
# SISTEMA DE VACACIONES CON SUPABASE
# ===================================================================

class SistemaVacacionesSupabase:
    def __init__(self):
        self.supabase = obtener_cliente_supabase()
        self.auth = SistemaAutenticacionSupabase()
        if self.supabase:
            self.crear_empleados_default()
    
    def crear_empleados_default(self):
        """Crea empleados por defecto"""
        empleados_default = [
            {
                "nombre_completo": "Juan Pérez",
                "total_dias": 22,
                "dias_usados": 5,
                "departamento": "Desarrollo",
                "activo": True
            },
            {
                "nombre_completo": "María García",
                "total_dias": 22,
                "dias_usados": 3,
                "departamento": "Marketing",
                "activo": True
            },
            {
                "nombre_completo": "Administrador del Sistema",
                "total_dias": 22,
                "dias_usados": 0,
                "departamento": "Administración",
                "activo": True
            },
            {
                "nombre_completo": "Recursos Humanos",
                "total_dias": 22,
                "dias_usados": 0,
                "departamento": "RRHH",
                "activo": True
            }
        ]
        
        for empleado in empleados_default:
            try:
                existing = self.supabase.table('empleados')\
                    .select('id')\
                    .eq('nombre_completo', empleado['nombre_completo'])\
                    .execute()
                if not existing.data:
                    self.supabase.table('empleados').insert(empleado).execute()
            except:
                continue
    
    def obtener_empleados(self):
        """Obtiene todos los empleados activos"""
        if not self.supabase:
            return {}
        
        try:
            result = self.supabase.table('empleados')\
                .select('*')\
                .eq('activo', True)\
                .execute()
            
            # Convertir a formato dict para compatibilidad
            empleados = {}
            for emp in result.data:
                empleados[emp['nombre_completo']] = {
                    'id': emp['id'],
                    'total_dias': emp['total_dias'],
                    'dias_usados': emp['dias_usados'],
                    'departamento': emp['departamento']
                }
            return empleados
        except:
            return {}
    
    def obtener_solicitudes(self):
        """Obtiene todas las solicitudes"""
        if not self.supabase:
            return []
        
        try:
            result = self.supabase.table('solicitudes_vacaciones')\
                .select('*, empleados(nombre_completo, departamento)')\
                .order('fecha_creacion', desc=True)\
                .execute()
            
            # Convertir formato para compatibilidad
            solicitudes = []
            for sol in result.data:
                solicitudes.append({
                    'id': sol['id'],
                    'usuario': sol['empleados']['nombre_completo'],
                    'fecha_inicio': sol['fecha_inicio'],
                    'fecha_fin': sol['fecha_fin'],
                    'dias_solicitados': sol['dias_solicitados'],
                    'estado': sol['estado'],
                    'fecha_creacion': sol['fecha_creacion'],
                    'creado_por': sol.get('creado_por', ''),
                    'aprobado_por': sol.get('aprobado_por', ''),
                    'fecha_aprobacion': sol.get('fecha_aprobacion', '')
                })
            return solicitudes
        except:
            return []
    
    def crear_solicitud(self, usuario_actual, empleado, fecha_inicio, fecha_fin):
        """Crea solicitud de vacaciones"""
        if not self.supabase:
            return False, "Error de conexión"
        
        # Validaciones
        if fecha_inicio > fecha_fin:
            return False, "La fecha de inicio no puede ser posterior a la fecha de fin"
        
        if fecha_inicio < datetime.date.today():
            return False, "No se pueden solicitar vacaciones en fechas pasadas"
        
        dias_solicitados = (fecha_fin - fecha_inicio).days + 1
        
        try:
            # Buscar empleado
            empleado_result = self.supabase.table('empleados')\
                .select('*')\
                .eq('nombre_completo', empleado)\
                .eq('activo', True)\
                .execute()
            
            if not empleado_result.data:
                return False, "Empleado no encontrado"
            
            empleado_data = empleado_result.data[0]
            dias_disponibles = empleado_data['total_dias'] - empleado_data['dias_usados']
            
            if dias_solicitados > dias_disponibles:
                return False, f"Solo hay {dias_disponibles} días disponibles"
            
            # Crear solicitud
            nueva_solicitud = {
                "empleado_id": empleado_data['id'],
                "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
                "dias_solicitados": dias_solicitados,
                "estado": "pendiente",
                "creado_por": usuario_actual["nombre_completo"],
                "comentarios": ""
            }
            
            self.supabase.table('solicitudes_vacaciones').insert(nueva_solicitud).execute()
            
            # Registrar auditoría
            self.registrar_auditoria(
                usuario_actual["nombre_completo"],
                "solicitud_creada",
                f"Solicitud para {empleado} de {dias_solicitados} días"
            )
            
            return True, "Solicitud creada exitosamente"
        
        except Exception as e:
            return False, f"Error creando solicitud: {e}"
    
    def aprobar_solicitud(self, solicitud_id, usuario_actual):
        """Aprueba una solicitud"""
        if not self.supabase:
            return False
        
        try:
            # Obtener solicitud con empleado
            solicitud_result = self.supabase.table('solicitudes_vacaciones')\
                .select('*, empleados(id, dias_usados)')\
                .eq('id', solicitud_id)\
                .eq('estado', 'pendiente')\
                .execute()
            
            if not solicitud_result.data:
                return False
            
            solicitud = solicitud_result.data[0]
            empleado = solicitud['empleados']
            
            # Actualizar solicitud
            self.supabase.table('solicitudes_vacaciones')\
                .update({
                    "estado": "aprobado",
                    "aprobado_por": usuario_actual["nombre_completo"],
                    "fecha_aprobacion": datetime.datetime.now().isoformat()
                })\
                .eq('id', solicitud_id)\
                .execute()
            
            # Actualizar días usados del empleado
            nuevos_dias = empleado['dias_usados'] + solicitud['dias_solicitados']
            self.supabase.table('empleados')\
                .update({"dias_usados": nuevos_dias})\
                .eq('id', empleado['id'])\
                .execute()
            
            # Auditoría
            self.registrar_auditoria(
                usuario_actual["nombre_completo"],
                "solicitud_aprobada",
                f"Solicitud ID {solicitud_id}"
            )
            
            return True
        
        except Exception:
            return False
    
    def rechazar_solicitud(self, solicitud_id, usuario_actual):
        """Rechaza una solicitud"""
        if not self.supabase:
            return False
        
        try:
            # Actualizar solicitud
            self.supabase.table('solicitudes_vacaciones')\
                .update({
                    "estado": "rechazado",
                    "aprobado_por": usuario_actual["nombre_completo"],
                    "fecha_aprobacion": datetime.datetime.now().isoformat()
                })\
                .eq('id', solicitud_id)\
                .eq('estado', 'pendiente')\
                .execute()
            
            # Auditoría
            self.registrar_auditoria(
                usuario_actual["nombre_completo"],
                "solicitud_rechazada",
                f"Solicitud ID {solicitud_id}"
            )
            
            return True
        
        except Exception:
            return False
    
    def registrar_auditoria(self, usuario, accion, detalle=""):
        """Registra acción en auditoría"""
        if not self.supabase:
            return
        
        try:
            auditoria_data = {
                "usuario": usuario,
                "accion": accion,
                "detalle": detalle
            }
            
            self.supabase.table('auditoria').insert(auditoria_data).execute()
        except:
            pass

# ===================================================================
# PÁGINAS DE LA INTERFAZ
# ===================================================================

def pagina_registro_publico():
    """Página pública para solicitar registro"""
    st.title("📝 Solicitar Acceso al Sistema")
    st.markdown("Completa este formulario para solicitar acceso al sistema de vacaciones")
    
    with st.form("formulario_registro"):
        col1, col2 = st.columns(2)
        
        with col1:
            nombre_completo = st.text_input("👤 Nombre Completo*")
            email = st.text_input("📧 Email Corporativo*")
        
        with col2:
            departamento = st.selectbox("🏢 Cargo/Especialidad*", [
    "", "TENS", "ENFERMERO", "AUXILIAR"
])
            
        comentarios = st.text_area("💬 Comentarios adicionales", 
                                 placeholder="Ej: Soy el nuevo desarrollador que ingresó el 1 de octubre...")
        
        submitted = st.form_submit_button("📤 Enviar Solicitud", type="primary")
        
        if submitted:
            if nombre_completo and email and departamento:
                auth = SistemaAutenticacionSupabase()
                exito, mensaje = auth.crear_solicitud_registro(
                    nombre_completo, email, departamento, comentarios
                )
                
                if exito:
                    st.success(mensaje)
                    st.info("📋 Tu solicitud será revisada por el jefatura de enfermería.")
                    st.balloons()
                else:
                    st.error(mensaje)
            else:
                st.error("Por favor completa todos los campos obligatorios (*)")

def pagina_login_mejorada():
    """Login mejorado con mejor seguridad"""
    
    # Header con logo y título
    col1, col2 = st.columns([1, 4])
    
    with col1:
        try:
            st.image("logoUci.png", width=80)
        except:
            st.write("🏥")  # Fallback si no encuentra la imagen
    
    with col2:
        st.title("Sistema de Vacaciones - Iniciar Sesión")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("👤 Usuario")
        password = st.text_input("🔒 Contraseña", type="password")
        
        if st.button("🚀 Iniciar Sesión", type="primary"):
            auth = SistemaAutenticacionSupabase()
            usuario, mensaje = auth.autenticar_mejorado(username, password)
            
            if usuario:
                st.session_state.usuario_logueado = usuario
                st.session_state.username = username
                st.success(mensaje)
                st.rerun()
            else:
                st.error(mensaje)
        
        with st.expander("👥 Usuarios de Prueba"):
            st.markdown("""
            **🔑 Administrador:**
            - Usuario: `admin`
            - Contraseña: `admin123`
            
            **👔 Recursos Humanos:**
            - Usuario: `rrhh`
            - Contraseña: `rrhh123`
            
            **👤 Empleados:**
            - Usuario: `juan.perez` / Contraseña: `123456`
            - Usuario: `maria.garcia` / Contraseña: `123456`
            """)

def mostrar_dashboard(sistema, usuario, permisos):
    """Dashboard principal"""
    st.header("📊 Dashboard")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    solicitudes = sistema.obtener_solicitudes()
    total = len(solicitudes)
    pendientes = len([s for s in solicitudes if s["estado"] == "pendiente"])
    aprobadas = len([s for s in solicitudes if s["estado"] == "aprobado"])
    rechazadas = len([s for s in solicitudes if s["estado"] == "rechazado"])
    
    with col1:
        st.metric("📝 Total Solicitudes", total)
    with col2:
        st.metric("⏳ Pendientes", pendientes)
    with col3:
        st.metric("✅ Aprobadas", aprobadas)
    with col4:
        st.metric("❌ Rechazadas", rechazadas)
    
    st.markdown("---")
    
    # Estado de empleados
    if permisos["ver_todas_solicitudes"]:
        st.subheader("👥 Estado de Empleados")
        
        empleados = sistema.obtener_empleados()
        for nombre, datos in empleados.items():
            col1, col2, col3, col4 = st.columns(4)
            
            disponibles = datos["total_dias"] - datos["dias_usados"]
            porcentaje = (datos["dias_usados"] / datos["total_dias"]) * 100
            
            with col1:
                st.write(f"**{nombre}**")
            with col2:
                st.write(f"Depto: {datos['departamento']}")
            with col3:
                st.write(f"Usados: {datos['dias_usados']}/{datos['total_dias']}")
            with col4:
                st.progress(porcentaje/100)
        
    else:
        # Vista de empleado
        if usuario["empleado_asociado"]:
            st.subheader("📊 Tus Vacaciones")
            empleados = sistema.obtener_empleados()
            empleado_data = empleados.get(usuario["empleado_asociado"], {})
            
            if empleado_data:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Días Totales", empleado_data.get("total_dias", 0))
                with col2:
                    st.metric("Días Usados", empleado_data.get("dias_usados", 0))
                with col3:
                    disponibles = empleado_data.get("total_dias", 0) - empleado_data.get("dias_usados", 0)
                    st.metric("Días Disponibles", disponibles)

def mostrar_nueva_solicitud(sistema, usuario):
    """Formulario para nueva solicitud"""
    st.header("📝 Nueva Solicitud de Vacaciones")
    
    empleados = sistema.obtener_empleados()
    
    if usuario["rol"] == "empleado":
        empleado_seleccionado = usuario["empleado_asociado"]
        st.info(f"👤 Creando solicitud para: **{empleado_seleccionado}**")
    else:
        empleados_list = list(empleados.keys())
        empleado_seleccionado = st.selectbox("👤 Seleccionar Empleado", empleados_list)
    
    if empleado_seleccionado and empleado_seleccionado in empleados:
        datos_empleado = empleados[empleado_seleccionado]
        dias_disponibles = datos_empleado["total_dias"] - datos_empleado["dias_usados"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"💼 Días disponibles: **{dias_disponibles}**")
        with col2:
            st.info(f"🏢 Departamento: **{datos_empleado['departamento']}**")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            fecha_inicio = st.date_input("📅 Fecha de Inicio", min_value=datetime.date.today())
        with col2:
            fecha_fin = st.date_input("📅 Fecha de Fin", min_value=datetime.date.today())
        
        if fecha_inicio and fecha_fin and fecha_inicio <= fecha_fin:
            dias_solicitados = (fecha_fin - fecha_inicio).days + 1
            
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"📝 Días a solicitar: **{dias_solicitados}**")
            with col2:
                if dias_solicitados <= dias_disponibles:
                    st.success("✅ Días suficientes")
                else:
                    st.error("❌ Días insuficientes")
        
        if st.button("🚀 Crear Solicitud", type="primary"):
            if fecha_inicio and fecha_fin:
                exito, mensaje = sistema.crear_solicitud(usuario, empleado_seleccionado, fecha_inicio, fecha_fin)
                if exito:
                    st.success(mensaje)
                    st.balloons()
                    st.rerun()
                else:
                    st.error(mensaje)
            else:
                st.error("❌ Por favor completa todas las fechas")

def mostrar_solicitudes(sistema, usuario, permisos):
    """Muestra solicitudes según permisos"""
    st.header("📋 Gestión de Solicitudes")
    
    solicitudes = sistema.obtener_solicitudes()
    
    # Filtrar según permisos
    if not permisos["ver_todas_solicitudes"]:
        solicitudes = [s for s in solicitudes if s["usuario"] == usuario["empleado_asociado"]]
    
    if not solicitudes:
        st.info("📝 No hay solicitudes para mostrar")
        return
    
    # Filtros para admin/rrhh
    if permisos["ver_todas_solicitudes"]:
        col1, col2 = st.columns(2)
        with col1:
            filtro_estado = st.selectbox("🔍 Filtrar por Estado", ["Todos", "pendiente", "aprobado", "rechazado"])
        with col2:
            empleados = sistema.obtener_empleados()
            filtro_usuario = st.selectbox("🔍 Filtrar por Usuario", ["Todos"] + list(empleados.keys()))
        
        # Aplicar filtros
        if filtro_estado != "Todos":
            solicitudes = [s for s in solicitudes if s["estado"] == filtro_estado]
        if filtro_usuario != "Todos":
            solicitudes = [s for s in solicitudes if s["usuario"] == filtro_usuario]
    
    st.markdown("---")
    
    # Mostrar solicitudes
    for solicitud in solicitudes:
        with st.container():
            # Color según estado
            if solicitud["estado"] == "pendiente":
                st.warning(f"⏳ **Solicitud #{solicitud['id']} - PENDIENTE**")
            elif solicitud["estado"] == "aprobado":
                st.success(f"✅ **Solicitud #{solicitud['id']} - APROBADA**")
            else:
                st.error(f"❌ **Solicitud #{solicitud['id']} - RECHAZADA**")
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"""
                **👤 Empleado:** {solicitud['usuario']}
                
                **📅 Período:** {solicitud['fecha_inicio']} → {solicitud['fecha_fin']}
                
                **📝 Días:** {solicitud['dias_solicitados']} días
                
                **🕐 Creada:** {solicitud.get('fecha_creacion', 'N/A')}
                
                **👨‍💼 Por:** {solicitud.get('creado_por', 'N/A')}
                """)
            
            # Botones para admin/rrhh
            if permisos["aprobar_solicitudes"] and solicitud["estado"] == "pendiente":
                with col2:
                    if st.button(f"✅ Aprobar", key=f"aprobar_{solicitud['id']}"):
                        if sistema.aprobar_solicitud(solicitud['id'], usuario):
                            st.success("✅ Solicitud aprobada")
                            st.rerun()
                
                with col3:
                    if st.button(f"❌ Rechazar", key=f"rechazar_{solicitud['id']}"):
                        if sistema.rechazar_solicitud(solicitud['id'], usuario):
                            st.error("❌ Solicitud rechazada")
                            st.rerun()
            
            st.markdown("---")

def mostrar_empleados(sistema, usuario):
    """Gestión de empleados"""
    st.header("👥 Gestión de Empleados")
    
    st.subheader("Empleados Actuales")
    
    empleados = sistema.obtener_empleados()
    
    # Crear tabla
    empleados_data = []
    for nombre, datos in empleados.items():
        disponibles = datos["total_dias"] - datos["dias_usados"]
        empleados_data.append({
            "Nombre": nombre,
            "Departamento": datos["departamento"],
            "Días Totales": datos["total_dias"],
            "Días Usados": datos["dias_usados"],
            "Días Disponibles": disponibles
        })
    
    if empleados_data:
        df = pd.DataFrame(empleados_data)
        st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    
    # Agregar nuevo empleado
    st.subheader("➕ Agregar Nuevo Empleado")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nuevo_nombre = st.text_input("Nombre completo")
    with col2:
        nuevo_departamento = st.text_input("Departamento")
    with col3:
        nuevos_dias = st.number_input("Días anuales", min_value=1, max_value=365, value=22)
    
    if st.button("➕ Agregar Empleado"):
        if nuevo_nombre and nuevo_departamento:
            if nuevo_nombre not in empleados:
                try:
                    empleado_data = {
                        "nombre_completo": nuevo_nombre,
                        "total_dias": nuevos_dias,
                        "dias_usados": 0,
                        "departamento": nuevo_departamento,
                        "activo": True
                    }
                    sistema.supabase.table('empleados').insert(empleado_data).execute()
                    sistema.registrar_auditoria(
                        usuario["nombre_completo"],
                        "empleado_agregado",
                        f"Empleado {nuevo_nombre} en {nuevo_departamento}"
                    )
                    st.success(f"✅ Empleado {nuevo_nombre} agregado exitosamente")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error agregando empleado: {e}")
            else:
                st.error("❌ El empleado ya existe")
        else:
            st.error("❌ Completa todos los campos")

def pagina_gestion_solicitudes_registro(usuario_admin):
    """Página para que admin gestione solicitudes de registro"""
    st.header("📋 Gestión de Solicitudes de Registro")
    
    auth = SistemaAutenticacionSupabase()
    solicitudes = auth.obtener_solicitudes_registro()
    
    # Filtrar solicitudes pendientes
    pendientes = [s for s in solicitudes if s["estado"] == "pendiente"]
    
    if not pendientes:
        st.info("📝 No hay solicitudes pendientes")
        
        # Mostrar historial
        if st.checkbox("Ver historial de solicitudes"):
            historial = [s for s in solicitudes if s["estado"] != "pendiente"]
            
            for solicitud in historial:
                estado_emoji = "✅" if solicitud["estado"] == "aprobada" else "❌"
                fecha_solicitud = solicitud.get('fecha_solicitud', '')
                if fecha_solicitud:
                    fecha_solicitud = fecha_solicitud[:10]
                
                st.markdown(f"""
                **{estado_emoji} {solicitud['nombre_completo']}** - {solicitud['estado'].title()}
                
                📧 {solicitud['email']} | 🏢 {solicitud['Estamento']}
                
                📅 Solicitado: {fecha_solicitud}
                
                ---
                """)
        return
    
    st.markdown(f"**{len(pendientes)} solicitudes pendientes de revisión**")
    
    for solicitud in pendientes:
        with st.container():
            st.markdown(f"### 👤 {solicitud['nombre_completo']}")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                fecha_solicitud = solicitud.get('fecha_solicitud', '')
                if fecha_solicitud:
                    fecha_solicitud = fecha_solicitud[:10]
                
                st.markdown(f"""
                **📧 Email:** {solicitud['email']}
                
                **🏢 Departamento:** {solicitud['departamento']}
                
                **📅 Fecha solicitud:** {fecha_solicitud}
                
                **💬 Comentarios:** {solicitud.get('comentarios', 'Sin comentarios')}
                """)
            
            with col2:
                # Password temporal personalizada
                password_temp = st.text_input(
                    f"Password temporal para {solicitud['nombre_completo']}", 
                    value=f"temp{datetime.datetime.now().strftime('%m%d')}",
                    key=f"pass_{solicitud['id']}"
                )
                
                col_aprobar, col_rechazar = st.columns(2)
                
                with col_aprobar:
                    if st.button(f"✅ Aprobar", key=f"aprobar_{solicitud['id']}"):
                        exito, mensaje = auth.procesar_solicitud_registro(
                            solicitud['id'], 
                            "aprobar", 
                            usuario_admin,
                            password_temp
                        )
                        if exito:
                            st.success(mensaje)
                            st.rerun()
                        else:
                            st.error(mensaje)
                
                with col_rechazar:
                    if st.button(f"❌ Rechazar", key=f"rechazar_{solicitud['id']}"):
                        exito, mensaje = auth.procesar_solicitud_registro(
                            solicitud['id'], 
                            "rechazar", 
                            usuario_admin
                        )
                        if exito:
                            st.success(mensaje)
                            st.rerun()
                        else:
                            st.error(mensaje)
            
            st.markdown("---")

def mostrar_menu_con_registro():
    """Menú principal con opción de registro"""
    if "usuario_logueado" not in st.session_state:
        # Página de login con opción de registro
        tab1, tab2 = st.tabs(["🔐 Iniciar Sesión", "📝 Solicitar Acceso"])
        
        with tab1:
            pagina_login_mejorada()
        
        with tab2:
            pagina_registro_publico()
    else:
        # Usuario logueado - mostrar app completa
        pagina_principal_completa()

def pagina_principal_completa():
    """App principal completa con todas las funcionalidades"""
    usuario = st.session_state.usuario_logueado
    username = st.session_state.username
    
    # Header principal
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("Sistema de Gestión de Vacaciones UPC Quirúrgica")
        st.markdown(f"**👤** {usuario.get('nombre_completo', 'Usuario')} | **🎭** {usuario.get('rol', 'empleado').replace('_', ' ').title()}")
        st.caption("🌐 Usando Supabase (Base de datos en la nube)")
    
    with col2:
        if st.button("🚪 Cerrar Sesión"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown("---")
    
    # Obtener permisos
    auth = SistemaAutenticacionSupabase()
    permisos = auth.obtener_permisos(usuario.get("rol", "empleado"))
    
    # Crear tabs según permisos
    tabs_disponibles = []
    if permisos["ver_dashboard"]:
        tabs_disponibles.append("📊 Dashboard")
    if permisos["crear_solicitudes"] or usuario["rol"] == "administrador":
        tabs_disponibles.append("📝 Nueva Solicitud")
    if permisos["ver_todas_solicitudes"] or usuario["rol"] == "empleado":
        tabs_disponibles.append("📋 Solicitudes")
    if permisos["gestionar_empleados"]:
        tabs_disponibles.append("👥 Empleados")
    if permisos["gestionar_usuarios"]:
        tabs_disponibles.append("🆕 Solicitudes Registro")
    
    # Crear tabs
    tabs = st.tabs(tabs_disponibles)
    
    # Inicializar sistema
    sistema = SistemaVacacionesSupabase()
    
    # Dashboard
    if "📊 Dashboard" in tabs_disponibles:
        with tabs[tabs_disponibles.index("📊 Dashboard")]:
            mostrar_dashboard(sistema, usuario, permisos)
    
    # Nueva Solicitud
    if "📝 Nueva Solicitud" in tabs_disponibles:
        with tabs[tabs_disponibles.index("📝 Nueva Solicitud")]:
            mostrar_nueva_solicitud(sistema, usuario)
    
    # Solicitudes
    if "📋 Solicitudes" in tabs_disponibles:
        with tabs[tabs_disponibles.index("📋 Solicitudes")]:
            mostrar_solicitudes(sistema, usuario, permisos)
    
    # Empleados
    if "👥 Empleados" in tabs_disponibles:
        with tabs[tabs_disponibles.index("👥 Empleados")]:
            mostrar_empleados(sistema, usuario)
    
    # Solicitudes de Registro
    if "🆕 Solicitudes Registro" in tabs_disponibles:
        with tabs[tabs_disponibles.index("🆕 Solicitudes Registro")]:
            pagina_gestion_solicitudes_registro(usuario)

# ===================================================================
# FUNCIÓN PRINCIPAL PARA CREAR TABLAS
# ===================================================================

def crear_tablas_supabase():
    """Crea todas las tablas necesarias en Supabase"""
    supabase = obtener_cliente_supabase()
    if not supabase:
        st.error("No se pudo conectar a Supabase")
        return
    
    st.info("📋 Ve a tu panel de Supabase → SQL Editor y ejecuta este código:")
    
    sql_completo = """
-- Tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    rol VARCHAR(50) NOT NULL,
    nombre_completo VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    empleado_asociado VARCHAR(200),
    departamento VARCHAR(100),
    activo BOOLEAN DEFAULT true,
    debe_cambiar_password BOOLEAN DEFAULT false,
    intentos_fallidos INTEGER DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT NOW(),
    ultimo_acceso TIMESTAMP
);

-- Tabla empleados
CREATE TABLE IF NOT EXISTS empleados (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre_completo VARCHAR(200) UNIQUE NOT NULL,
    total_dias INTEGER DEFAULT 22,
    dias_usados INTEGER DEFAULT 0,
    departamento VARCHAR(100) NOT NULL,
    fecha_ingreso DATE DEFAULT CURRENT_DATE,
    activo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tabla solicitudes_vacaciones
CREATE TABLE IF NOT EXISTS solicitudes_vacaciones (
    id SERIAL PRIMARY KEY,
    empleado_id UUID REFERENCES empleados(id),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    dias_solicitados INTEGER NOT NULL,
    estado VARCHAR(20) DEFAULT 'pendiente' 
        CHECK (estado IN ('pendiente', 'aprobado', 'rechazado')),
    fecha_creacion TIMESTAMP DEFAULT NOW(),
    creado_por VARCHAR(200),
    aprobado_por VARCHAR(200),
    fecha_aprobacion TIMESTAMP,
    comentarios TEXT
);

-- Tabla solicitudes_registro
CREATE TABLE IF NOT EXISTS solicitudes_registro (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre_completo VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL,
    departamento VARCHAR(100) NOT NULL,
    comentarios TEXT,
    estado VARCHAR(20) DEFAULT 'pendiente' 
        CHECK (estado IN ('pendiente', 'aprobada', 'rechazada')),
    fecha_solicitud TIMESTAMP DEFAULT NOW(),
    revisada_por VARCHAR(200),
    fecha_revision TIMESTAMP,
    username_asignado VARCHAR(100),
    password_temporal VARCHAR(50)
);

-- Tabla auditoria
CREATE TABLE IF NOT EXISTS auditoria (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario VARCHAR(200) NOT NULL,
    accion VARCHAR(100) NOT NULL,
    detalle TEXT,
    timestamp TIMESTAMP DEFAULT NOW()
);
"""
    
    st.code(sql_completo, language="sql")
    
    st.markdown("""
    **Pasos:**
    1. Ve a tu panel de Supabase
    2. Clic en **"SQL Editor"** en el sidebar
    3. Copia y pega el SQL de arriba
    4. Clic en **"RUN"**
    5. ¡Listo! Reinicia esta aplicación
    """)

# ===================================================================
# FUNCIÓN PRINCIPAL
# ===================================================================

def main():
    # Verificar si Supabase está configurado
    supabase = obtener_cliente_supabase()
    
    if not supabase:
        st.error("🚨 Supabase no configurado")
        st.markdown("Configure en `.streamlit/secrets.toml`:")
        st.code("""
[default]
SUPABASE_URL = "https://kolmoubvjxuqosqhylho.supabase.co"
SUPABASE_ANON_KEY = "tu_anon_key_aqui"
        """)
        return
    
    # Verificar si las tablas existen
    try:
        # Intentar consultar usuarios para verificar si las tablas existen
        result = supabase.table('usuarios').select('id').limit(1).execute()
        
        # Si llegamos aquí, las tablas existen
        # Crear usuarios por defecto
        auth = SistemaAutenticacionSupabase()
        auth.crear_usuarios_default()
        
        # Ejecutar la aplicación
        mostrar_menu_con_registro()
        
    except Exception as e:
        # Las tablas no existen
        st.error("🚨 Las tablas de Supabase no existen")
        st.markdown("Necesitas crear las tablas primero:")
        
        if st.button("📋 Mostrar SQL para crear tablas"):
            crear_tablas_supabase()

if __name__ == "__main__":
    main()