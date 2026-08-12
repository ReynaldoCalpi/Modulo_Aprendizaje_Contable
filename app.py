import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="ContaGo SV - Contabilidad desde Cero",
    page_icon="📊",
    layout="centered"
)

# Inicializar estado de sesión para el progreso del usuario
if "module_1_passed" not in st.session_state:
    st.session_state.module_1_passed = False

# ==========================================
# MENÚ LATERAL (SIDEBAR)
# ==========================================
st.sidebar.title("📊 ContaGo SV")
st.sidebar.markdown("**Contabilidad y Tributación - El Salvador**")
st.sidebar.markdown("---")

menu_options = [
    "🏠 Inicio", 
    "📚 Módulo 1: Contabilidad al Grano", 
    "💼 Módulo 2: Ley Laboral", 
    "🏛️ Módulo 3: Impuestos DGII"
]
choice = st.sidebar.selectbox("Selecciona una sección:", menu_options)

# Cálculo de progreso dinámico
progress = 25 if st.session_state.module_1_passed else 0
st.sidebar.markdown("---")
st.sidebar.text(f"Progreso General: {progress}%")
st.sidebar.progress(progress)


# ==========================================
# CONTENIDO DE LA APLICACIÓN
# ==========================================

if choice == "🏠 Inicio":
    st.title("Bienvenido a ContaGo SV 🚀")
    st.markdown("""
    Aprende contabilidad financiera, legislación laboral y fiscalidad de **El Salvador** de forma interactiva, 
    directa al grano y sin rodeos teóricos innecesarios.
    
    ### ¿Cómo funciona?
    1. **La Píldora:** Conceptos clave explicados de forma ultracorta.
    2. **El Laboratorio:** Simuladores y calculadoras para interactuar con los números.
    3. **El Reto:** Cuestionarios rápidos para validar tu aprendizaje y desbloquear contenidos.
    
    *Utiliza el menú lateral para empezar.*
    """)

elif choice == "📚 Módulo 1: Contabilidad al Grano":
    st.title("Módulo 1: Contabilidad al Gran Grano")
    st.markdown("Domina la lógica fundamental de los negocios en El Salvador.")
    
    # Pestañas secuenciales para evitar saturar la pantalla
    tab1, tab2, tab3 = st.tabs(["📖 La Píldora", "🧮 Laboratorio", "❓ El Reto"])
    
    with tab1:
        st.subheader("La Ecuación Contable")
        st.markdown("""
        En cualquier negocio, los recursos disponibles siempre deben cuadrar con su origen de financiamiento:
        
        **Activo = Pasivo + Patrimonio**
        
        *   **Activo:** Lo que la empresa *tiene* (efectivo en caja, inventarios, mobiliario).
        *   **Pasivo:** Lo que la empresa *debe* a terceros (préstamos bancarios, cuentas por pagar).
        *   **Patrimonio:** Lo que realmente *pertenece a los dueños* (capital inicial y utilidades retenidas).
        """)
        
    with tab2:
        st.subheader("Simulador de Equilibrio Patrimonial")
        st.markdown("Mueve los valores para ver cómo se comporta automáticamente el Activo total de una empresa:")
        
        col1, col2 = st.columns(2)
        with col1:
            pasivo = st.number_input("Pasivo (Deudas en $)", min_value=0.0, value=1200.0, step=100.0)
            patrimonio = st.number_input("Patrimonio (Capital en $)", min_value=0.0, value=3800.0, step=100.0)
        
        # Cálculo automático
        activo_calculado = pasivo + patrimonio
        
        with col2:
            st.markdown("### Resultado:")
            st.metric(label="Activo Total Obligatorio", value=f"${activo_calculado:,.2f}")
        
    with tab3:
        st.subheader("Cuestionario de Validación")
        st.markdown("Responde correctamente para certificar este módulo.")
        
        answer = st.radio(
            "¿Cuál es la fórmula fundamental que equilibra la contabilidad de una empresa?",
            (
                "Pasivo = Activo + Patrimonio",
                "Activo = Pasivo + Patrimonio",
                "Patrimonio = Activo + Pasivo"
            ),
            index=None
        )
        
        if st.button("Validar Respuesta"):
            if answer == "Activo = Pasivo + Patrimonio":
                st.success("¡Excelente! Has dominado la ecuación contable básica.")
                st.session_state.module_1_passed = True
            elif answer is None:
                st.warning("Por favor, selecciona una opción antes de validar.")
            else:
                st.error("Incorrecto. Recuerda que los bienes (Activos) se financian con deudas (Pasivos) y aportes propios (Patrimonio).")

elif choice == "💼 Módulo 2: Ley Laboral":
    st.title("Módulo 2: Ley Laboral y Planillas (El Salvador)")
    if not st.session_state.module_1_passed:
        st.warning("🔒 Este módulo está bloqueado. Debes completar y aprobar el **Módulo 1** primero.")
    else:
        st.success("¡Módulo desbloqueado con éxito! Aquí construiremos el calculador de AFP, ISSS y retenciones de ley.")

elif choice == "🏛️ Módulo 3: Impuestos DGII":
    st.title("Módulo 3: Tributación y DGII")
    st.info("Próximamente disponible al avanzar en los módulos anteriores.")