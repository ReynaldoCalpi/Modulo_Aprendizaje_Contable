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
if "module_2_passed" not in st.session_state:
    st.session_state.module_2_passed = False

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

# Cálculo de progreso dinámico (3 módulos en total)
completed_modules = sum([st.session_state.module_1_passed, st.session_state.module_2_passed])
progress = int((completed_modules / 3) * 100)

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
    1. **La Píldora:** Conceptos clave explicados con casos reales del mercado salvadoreño.
    2. **El Laboratorio:** Simuladores y clasificadores interactivos.
    3. **El Reto:** Cuestionarios prácticos para validar tu aprendizaje y desbloquear contenidos.
    
    *Utiliza el menú lateral para empezar.*
    """)

elif choice == "📚 Módulo 1: Contabilidad al Grano":
    st.title("Módulo 1: Fundamentos y Lógica Contable")
    st.markdown("Comprende la contabilidad no como una obligación aburrida, sino como el **GPS financiero** de cualquier emprendimiento o empresa en El Salvador.")
    
    tab1, tab2, tab3 = st.tabs(["📖 La Píldora y Caso Real", "🧮 Laboratorio: Clasificador", "❓ El Reto"])
    
    with tab1:
        st.subheader("💡 ¿Qué es la Contabilidad en la práctica?")
        st.markdown("""
        Imagina que abres una ferretería en Apopa o una distribuidora en San Salvador. Necesitas saber:
        * ¿Cuánto dinero tienes disponible?
        * ¿Cuánto le debes a tus proveedores?
        * ¿Estás ganando o perdiendo dinero al final del mes?
        
        La contabilidad es simplemente el sistema ordenado para **registrar, clasificar y resumir** todas estas operaciones en dinero.
        """)
        
        st.info("🏢 **Caso de Estudio Real:** Don Carlos abre su tienda de repuestos con **$5,000.00** ahorrados en efectivo, compra mercadería por **$3,000.00** al crédito con un proveedor local, y además le pide un préstamo al banco por **$2,000.00**.")
        
        st.markdown("### Los 3 Pilares del Negocio de Don Carlos:")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric(label="🟢 Activos (Lo que tiene)", value="$10,000.00", delta="Efectivo + Mercadería")
        with col_b:
            st.metric(label="🔴 Pasivos (Lo que debe)", value="$5,000.00", delta="Crédito + Préstamo")
        with col_c:
            st.metric(label="🔵 Patrimonio (Capital neto)", value="$5,000.00", delta="Aporte inicial")
            
        st.markdown("---")
        st.markdown("""
        **La Ecuación de Hierro:**
        $$\\text{Activo} (\\$10,000) = \\text{Pasivo} (\\$5,000) + \\text{Patrimonio} (\\$5,000)$$
        """)

    with tab2:
        st.subheader("🧮 Laboratorio: Clasifica la Cuenta")
        st.markdown("Pon a prueba tu intuición comercial. Selecciona a qué categoría pertenece cada elemento típico de una empresa salvadoreña:")
        
        item_ejemplo = st.selectbox(
            "¿A qué categoría pertenece un **Vehículo de reparto** comprado para la empresa?",
            ("Selecciona una opción...", "Activo (Bien/Derecho)", "Pasivo (Deuda)", "Patrimonio (Capital de los dueños)")
        )
        
        if item_ejemplo == "Activo (Bien/Derecho)":
            st.success("¡Correcto! Un vehículo de reparto es un bien físico propiedad de la empresa, por lo tanto es un Activo.")
        elif item_ejemplo != "Selecciona una opción...":
            st.error("Incorrecto. Piensa que el vehículo le pertenece a la empresa y le genera valor (es un bien).")
            
        st.markdown("---")
        st.markdown("### Tipos de Contabilidad que verás en El Salvador:")
        st.markdown("""
        1. **Contabilidad Financiera:** Para ver la salud del negocio y reportarla a socios o bancos.
        2. **Contabilidad Fiscal (Tributaria):** Estrictamente enfocada en cumplir con las reglas del **Ministerio de Hacienda (DGII)**.
        """)

    with tab3:
        st.subheader("Cuestionario de Validación - Módulo 1")
        st.markdown("Demuestra que dominas los fundamentos para desbloquear el módulo de Ley Laboral.")
        
        answer = st.radio(
            "Tomando como referencia el caso de Don Carlos, si una empresa adquiere una deuda con un proveedor por mercadería al crédito, ¿cómo se clasifica esa obligación?",
            (
                "Como un Activo, porque aumenta la mercadería.",
                "Como un Pasivo, porque representa una deuda u obligación con un tercero.",
                "Como Patrimonio, porque incrementa el capital de los dueños."
            ),
            index=None
        )
        
        if st.button("Validar Respuesta Módulo 1"):
            if answer == "Como un Pasivo, porque representa una deuda u obligación con un tercero.":
                st.success("¡Excelente! Has comprendido perfectamente la diferencia entre bienes, deudas y capital. ¡Módulo 1 superado y desbloqueado!")
                st.session_state.module_1_passed = True
            elif answer is None:
                st.warning("Por favor, selecciona una opción antes de validar.")
            else:
                st.error("Incorrecto. Recuerda que todo lo que la empresa *debe* a terceras personas (proveedores, bancos) se cataloga estrictamente como Pasivo.")

elif choice == "💼 Módulo 2: Ley Laboral":
    st.title("Módulo 2: Ley Laboral y Planillas (El Salvador)")
    
    if not st.session_state.module_1_passed:
        st.warning("🔒 Este módulo está bloqueado. Debes completar y aprobar el **Módulo 1** en la pestaña anterior primero.")
    else:
        tab1, tab2, tab3 = st.tabs(["📖 La Píldora", "🧮 Laboratorio de Planilla", "❓ El Reto"])
        
        with tab1:
            st.subheader("Deducciones Obligatorias del Empleado")
            st.markdown("""
            Todo salario formal en El Salvador sufre dos retenciones legales básicas directas del empleado:
            
            *   **AFP (Administradora de Fondos de Pensiones):** Se descuenta el **7.25%** del salario bruto total sin límite máximo.
            *   **ISSS (Instituto Salvadoreño del Seguro Social):** Se descuenta el **3.00%**, pero ojo: tiene un **tope máximo de retención basado en un sueldo de $1,000.00** (es decir, la retención máxima de ISSS por ley es de $30.00, aunque el empleado gane más de $1,000).
            """)
            
        with tab2:
            st.subheader("Calculadora de Retenciones (Cálculo Rápido)")
            st.markdown("Ingresa un salario bruto mensual para calcular los descuentos de ley y el salario líquido:")
            
            salario_bruto = st.number_input("Salario Bruto Mensual ($)", min_value=0.0, value=650.0, step=25.0)
            
            # Cálculos bajo ley salvadoreña
            afp = salario_bruto * 0.0725
            base_isss = min(salario_bruto, 1000.0)
            isss = base_isss * 0.03
            salario_liquido = salario_bruto - (afp + isss)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Descuento AFP (7.25%)", value=f"${afp:,.2f}")
                st.metric(label="Descuento ISSS (3%)", value=f"${isss:,.2f}")
            with col2:
                st.markdown("### Resumen:")
                st.metric(label="Total Deducciones", value=f"${(afp + isss):,.2f}")
                st.metric(label="Salario Líquido a Recibir", value=f"${salario_liquido:,.2f}")

        with tab3:
            st.subheader("Cuestionario de Validación - Ley Laboral")
            st.markdown("Valida tus conocimientos para avanzar al módulo de impuestos.")
            
            answer_m2 = st.radio(
                "¿Cuál es el porcentaje de retención laboral obligatorio destinado al fondo de pensiones (AFP) en El Salvador?",
                (
                    "3.00%",
                    "7.25%",
                    "10.00%"
                ),
                index=None
            )
            
            if st.button("Validar Respuesta Módulo 2"):
                if answer_m2 == "7.25%":
                    st.success("¡Correcto! El 7.25% corresponde a la AFP. ¡Módulo 2 superado!")
                    st.session_state.module_2_passed = True
                elif answer_m2 is None:
                    st.warning("Selecciona una opción para continuar.")
                else:
                    st.error("Incorrecto. Recuerda que el 3% es para el ISSS y el 7.25% para la AFP.")

elif choice == "🏛️ Módulo 3: Impuestos DGII":
    st.title("Módulo 3: Tributación y DGII (El Salvador)")
    
    if not st.session_state.module_2_passed:
        st.warning("🔒 Este módulo está bloqueado. Debes completar y aprobar el **Módulo 2** primero.")
    else:
        st.success("¡Bienvenido al último módulo! Aquí abordaremos el IVA (13%) y el Pago a Cuenta.")
